#!/usr/bin/env python3
"""
OpenWebUI Community Statistics Tool

Fetches and aggregates data for plugins/posts you've published on openwebui.com.

Usage:
    1. Set environment variables:
       - OPENWEBUI_API_KEY: Your API Key
       - OPENWEBUI_USER_ID: Your user ID
    2. Run: python scripts/openwebui_stats.py

Get API Key:
    Visit https://openwebui.com/settings/api to create an API Key (starts with sk-)

Get User ID:
    Obtain from the API request on your profile page, format: b15d1348-4347-42b4-b815-e053342d6cb0
"""

import os
import json
import requests
from datetime import datetime
from typing import Optional
from pathlib import Path

# Try to load .env file
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class OpenWebUIStats:
    """OpenWebUI Community Statistics Tool"""

    BASE_URL = "https://api.openwebui.com/api/v1"

    def __init__(self, api_key: str, user_id: Optional[str] = None):
        """
        Initialize the statistics tool

        Args:
            api_key: OpenWebUI API Key (JWT Token)
            user_id: User ID, if None will be parsed from token
        """
        self.api_key = api_key
        self.user_id = user_id or self._parse_user_id_from_token(api_key)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def _parse_user_id_from_token(self, token: str) -> str:
        """Parse user ID from JWT Token"""
        import base64

        try:
            # JWT format: header.payload.signature
            payload = token.split(".")[1]
            # Add padding
            padding = 4 - len(payload) % 4
            if padding != 4:
                payload += "=" * padding
            decoded = base64.urlsafe_b64decode(payload)
            data = json.loads(decoded)
            return data.get("id", "")
        except Exception as e:
            print(f"⚠️ Unable to parse user ID from Token: {e}")
            return ""

    def get_user_posts(self, sort: str = "new", page: int = 1) -> list:
        """
        Get list of user's published posts

        Args:
            sort: Sort order (new/top/hot)
            page: Page number

        Returns:
            List of posts
        """
        url = f"{self.BASE_URL}/posts/users/{self.user_id}"
        params = {"sort": sort, "page": page}

        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_all_posts(self, sort: str = "new") -> list:
        """Get all posts (auto-pagination)"""
        all_posts = []
        page = 1

        while True:
            posts = self.get_user_posts(sort=sort, page=page)
            if not posts:
                break
            all_posts.extend(posts)
            page += 1

        return all_posts

    def generate_stats(self, posts: list) -> dict:
        """Generate statistics data"""
        stats = {
            "total_posts": len(posts),
            "total_downloads": 0,
            "total_views": 0,
            "total_upvotes": 0,
            "total_downvotes": 0,
            "total_saves": 0,
            "total_comments": 0,
            "by_type": {},
            "posts": [],
            "user": {},  # User info
        }

        # Extract user info from the first post
        if posts and "user" in posts[0]:
            user = posts[0]["user"]
            stats["user"] = {
                "username": user.get("username", ""),
                "name": user.get("name", ""),
                "profile_url": f"https://openwebui.com/u/{user.get('username', '')}",
                "profile_image": user.get("profileImageUrl", ""),
                "followers": user.get("followerCount", 0),
                "following": user.get("followingCount", 0),
                "total_points": user.get("totalPoints", 0),
                "post_points": user.get("postPoints", 0),
                "comment_points": user.get("commentPoints", 0),
                "contributions": user.get("totalContributions", 0),
            }

        for post in posts:
            # Cumulative stats
            stats["total_downloads"] += post.get("downloads", 0)
            stats["total_views"] += post.get("views", 0)
            stats["total_upvotes"] += post.get("upvotes", 0)
            stats["total_downvotes"] += post.get("downvotes", 0)
            stats["total_saves"] += post.get("saveCount", 0)
            stats["total_comments"] += post.get("commentCount", 0)

            # Categorize by type
            post_type = post.get("data", {}).get("meta", {}).get("type", "unknown")
            if post_type not in stats["by_type"]:
                stats["by_type"][post_type] = 0
            stats["by_type"][post_type] += 1

            # Individual post info
            manifest = post.get("data", {}).get("meta", {}).get("manifest", {})
            created_at = datetime.fromtimestamp(post.get("createdAt", 0))
            updated_at = datetime.fromtimestamp(post.get("updatedAt", 0))

            stats["posts"].append(
                {
                    "title": post.get("title", ""),
                    "slug": post.get("slug", ""),
                    "type": post_type,
                    "version": manifest.get("version", ""),
                    "downloads": post.get("downloads", 0),
                    "views": post.get("views", 0),
                    "upvotes": post.get("upvotes", 0),
                    "saves": post.get("saveCount", 0),
                    "comments": post.get("commentCount", 0),
                    "created_at": created_at.strftime("%Y-%m-%d"),
                    "updated_at": updated_at.strftime("%Y-%m-%d"),
                    "url": f"https://openwebui.com/posts/{post.get('slug', '')}",
                }
            )

        # Sort by downloads
        stats["posts"].sort(key=lambda x: x["downloads"], reverse=True)

        return stats

    def print_stats(self, stats: dict):
        """Print statistics report to terminal"""
        print("\n" + "=" * 60)
        print("📊 OpenWebUI Community Statistics Report")
        print("=" * 60)
        print(f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Overview
        print("📈 Overview")
        print("-" * 40)
        print(f"  📝 Total Posts: {stats['total_posts']}")
        print(f"  ⬇️  Total Downloads: {stats['total_downloads']}")
        print(f"  👁️  Total Views: {stats['total_views']}")
        print(f"  👍 Total Upvotes: {stats['total_upvotes']}")
        print(f"  💾 Total Saves: {stats['total_saves']}")
        print(f"  💬 Total Comments: {stats['total_comments']}")
        print()

        # By type
        print("📂 By Type")
        print("-" * 40)
        for post_type, count in stats["by_type"].items():
            print(f"  • {post_type}: {count}")
        print()

        # Detailed list
        print("📋 Post List (sorted by downloads)")
        print("-" * 60)

        # Header
        print(f"{'Rank':<4} {'Title':<30} {'Downloads':<10} {'Views':<10} {'Upvotes':<8}")
        print("-" * 60)

        for i, post in enumerate(stats["posts"], 1):
            title = (
                post["title"][:28] + ".." if len(post["title"]) > 28 else post["title"]
            )
            print(
                f"{i:<4} {title:<30} {post['downloads']:<10} {post['views']:<10} {post['upvotes']:<8}"
            )

        print("=" * 60)

    def generate_markdown(self, stats: dict) -> str:
        """Generate Markdown format report"""
        md = []
        md.append("# 📊 OpenWebUI Community Statistics Report")
        md.append("")
        md.append(f"> 📅 Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append("")

        # Overview
        md.append("## 📈 Overview")
        md.append("")
        md.append("| Metric | Value |")
        md.append("|------|------|")
        md.append(f"| 📝 Total Posts | {stats['total_posts']} |")
        md.append(f"| ⬇️ Total Downloads | {stats['total_downloads']} |")
        md.append(f"| 👁️ Total Views | {stats['total_views']} |")
        md.append(f"| 👍 Total Upvotes | {stats['total_upvotes']} |")
        md.append(f"| 💾 Total Saves | {stats['total_saves']} |")
        md.append(f"| 💬 Total Comments | {stats['total_comments']} |")
        md.append("")

        # By type
        md.append("## 📂 By Type")
        md.append("")
        for post_type, count in stats["by_type"].items():
            md.append(f"- **{post_type}**: {count}")
        md.append("")

        # Detailed list
        md.append("## 📋 Post List")
        md.append("")
        md.append(
            "| Rank | Title | Type | Version | Downloads | Views | Upvotes | Saves | Updated |"
        )
        md.append("|:---:|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")

        for i, post in enumerate(stats["posts"], 1):
            title_link = f"[{post['title']}]({post['url']})"
            md.append(
                f"| {i} | {title_link} | {post['type']} | {post['version']} | "
                f"{post['downloads']} | {post['views']} | {post['upvotes']} | "
                f"{post['saves']} | {post['updated_at']} |"
            )

        md.append("")
        return "\n".join(md)

    def save_json(self, stats: dict, filepath: str):
        """Save JSON format data"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON data saved to: {filepath}")

    def generate_readme_stats(self, stats: dict, lang: str = "en") -> str:
        """
        Generate README statistics badge section

        Args:
            stats: Statistics data
            lang: Language ("zh" Chinese, "en" English)
        """
        # Get Top 5 plugins
        top_plugins = stats["posts"][:5]

        # English text (default)
        t = {
            "title": "## 📊 Community Stats",
            "updated": f"> 🕐 Auto-updated on {datetime.now().strftime('%Y-%m-%d')}",
            "author_header": "| 👤 Author | 👥 Followers | ⭐ Points | 🏆 Contributions |",
            "header": "| 📝 Posts | ⬇️ Downloads | 👁️ Views | 👍 Upvotes | 💾 Saves |",
            "top5_title": "### 🔥 Top 5 Popular Plugins",
            "top5_header": "| Rank | Plugin | Downloads | Views |",
            "full_stats": "*See full stats in [Community Stats Report](./docs/community-stats.md)*",
        }
        user = stats.get("user", {})

        lines = []
        lines.append("<!-- STATS_START -->")
        lines.append(t["title"])
        lines.append("")
        lines.append(t["updated"])
        lines.append("")

        # Author info table
        if user:
            username = user.get("username", "")
            profile_url = user.get("profile_url", "")
            lines.append(t["author_header"])
            lines.append("|:---:|:---:|:---:|:---:|")
            lines.append(
                f"| [{username}]({profile_url}) | **{user.get('followers', 0)}** | "
                f"**{user.get('total_points', 0)}** | **{user.get('contributions', 0)}** |"
            )
            lines.append("")

        # Stats badge table
        lines.append(t["header"])
        lines.append("|:---:|:---:|:---:|:---:|:---:|")
        lines.append(
            f"| **{stats['total_posts']}** | **{stats['total_downloads']}** | "
            f"**{stats['total_views']}** | **{stats['total_upvotes']}** | **{stats['total_saves']}** |"
        )
        lines.append("")

        # Top 5 popular plugins
        lines.append(t["top5_title"])
        lines.append("")
        lines.append(t["top5_header"])
        lines.append("|:---:|------|:---:|:---:|")

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
        for i, post in enumerate(top_plugins):
            medal = medals[i] if i < len(medals) else str(i + 1)
            lines.append(
                f"| {medal} | [{post['title']}]({post['url']}) | {post['downloads']} | {post['views']} |"
            )

        lines.append("")
        lines.append(t["full_stats"])
        lines.append("<!-- STATS_END -->")

        return "\n".join(lines)

    def update_readme(self, stats: dict, readme_path: str, lang: str = "en"):
        """
        Update the statistics section in README file

        Args:
            stats: Statistics data
            readme_path: README file path
            lang: Language ("zh" Chinese, "en" English)
        """
        import re

        # Read existing content
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Generate new stats section
        new_stats = self.generate_readme_stats(stats, lang)

        # Check if stats section already exists
        pattern = r"<!-- STATS_START -->.*?<!-- STATS_END -->"
        if re.search(pattern, content, re.DOTALL):
            # Replace existing section
            new_content = re.sub(pattern, new_stats, content, flags=re.DOTALL)
        else:
            # Insert stats section after intro paragraph
            # Look for pattern: title -> language switch line -> intro paragraph -> insert position
            lines = content.split("\n")
            insert_pos = 0
            found_intro = False

            for i, line in enumerate(lines):
                # Skip title
                if line.startswith("# "):
                    continue
                # Skip empty lines
                if line.strip() == "":
                    continue
                # Skip language switch line (like "English | [中文]" or "[English] | 中文")
                if ("English" in line or "中文" in line) and "|" in line:
                    continue
                # Found the first non-empty, non-title, non-language-switch paragraph (intro)
                if not found_intro:
                    found_intro = True
                    # Continue to end of this paragraph
                    continue
                # Empty line or next heading after intro is the insert position
                if line.strip() == "" or line.startswith("#"):
                    insert_pos = i
                    break

            # If no suitable position found, place after line 3 (after title and language switch)
            if insert_pos == 0:
                insert_pos = 3

            # Insert at appropriate position
            lines.insert(insert_pos, "")
            lines.insert(insert_pos + 1, new_stats)
            lines.insert(insert_pos + 2, "")
            new_content = "\n".join(lines)

        # Write back to file
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ README updated: {readme_path}")


def main():
    """Main function"""
    # Get configuration
    api_key = os.getenv("OPENWEBUI_API_KEY")
    user_id = os.getenv("OPENWEBUI_USER_ID")

    if not api_key:
        print("❌ Error: OPENWEBUI_API_KEY environment variable not set")
        print("Please set environment variable:")
        print("  export OPENWEBUI_API_KEY='your_api_key_here'")
        return 1

    if not user_id:
        print("❌ Error: OPENWEBUI_USER_ID environment variable not set")
        print("Please set environment variable:")
        print("  export OPENWEBUI_USER_ID='your_user_id_here'")
        print("\nHint: User ID can be obtained from previous curl request")
        print("     Example: b15d1348-4347-42b4-b815-e053342d6cb0")
        return 1

    # Initialize
    stats_client = OpenWebUIStats(api_key, user_id)
    print(f"🔍 User ID: {stats_client.user_id}")

    # Get all posts
    print("📥 Fetching post data...")
    posts = stats_client.get_all_posts()
    print(f"✅ Retrieved {len(posts)} posts")

    # Generate stats
    stats = stats_client.generate_stats(posts)

    # Print to terminal
    stats_client.print_stats(stats)

    # Save Markdown report
    script_dir = Path(__file__).parent.parent
    md_path = script_dir / "docs" / "community-stats.md"
    md_content = stats_client.generate_markdown(stats)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"\n✅ Markdown report saved to: {md_path}")

    # Save JSON data
    json_path = script_dir / "docs" / "community-stats.json"
    stats_client.save_json(stats, str(json_path))

    # Update README file
    readme_path = script_dir / "README.md"
    stats_client.update_readme(stats, str(readme_path), lang="en")

    return 0


if __name__ == "__main__":
    exit(main())
