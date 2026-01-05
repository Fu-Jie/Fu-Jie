#!/usr/bin/env python3
"""
OpenWebUI 社区统计工具

获取并统计你在 openwebui.com 上发布的插件/帖子数据。

使用方法：
    1. 设置环境变量：
       - OPENWEBUI_API_KEY: 你的 API Key
       - OPENWEBUI_USER_ID: 你的用户 ID
    2. 运行: python scripts/openwebui_stats.py

获取 API Key：
    访问 https://openwebui.com/settings/api 创建 API Key (sk-开头)

获取 User ID：
    从个人主页的 API 请求中获取，格式如: b15d1348-4347-42b4-b815-e053342d6cb0
"""

import base64
import binascii
import os
import json
import requests
from datetime import datetime
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

load_dotenv()


class OpenWebUIStats:
    """OpenWebUI 社区统计工具"""

    BASE_URL = "https://api.openwebui.com/api/v1"

    def __init__(self, api_key: str, user_id: Optional[str] = None):
        """
        初始化统计工具

        Args:
            api_key: OpenWebUI API Key (JWT Token)
            user_id: 用户 ID，如果为 None 则从 token 中解析
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
        """从 JWT Token 中解析用户 ID"""
        try:
            # JWT 格式: header.payload.signature
            payload = token.split(".")[1]
            # 添加 padding
            padding = 4 - len(payload) % 4
            if padding != 4:
                payload += "=" * padding
            decoded = base64.urlsafe_b64decode(payload)
            data = json.loads(decoded)
            return data.get("id", "")
        except (IndexError, ValueError, json.JSONDecodeError, binascii.Error) as e:
            print(f"⚠️ 无法从 Token 解析用户 ID: {e}")
            return ""

    def get_user_posts(self, sort: str = "new", page: int = 1) -> list:
        """
        获取用户发布的帖子列表

        Args:
            sort: 排序方式 (new/top/hot)
            page: 页码

        Returns:
            帖子列表
        """
        url = f"{self.BASE_URL}/posts/users/{self.user_id}"
        params = {"sort": sort, "page": page}

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            status = getattr(exc.response, "status_code", "unknown")
            print(f"❌ 获取帖子数据失败 (HTTP {status}): {exc}")
            raise
        return response.json()

    def get_all_posts(self, sort: str = "new") -> list:
        """获取所有帖子（自动分页）"""
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
        """生成统计数据"""
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
        }

        for post in posts:
            # 累计统计
            stats["total_downloads"] += post.get("downloads", 0)
            stats["total_views"] += post.get("views", 0)
            stats["total_upvotes"] += post.get("upvotes", 0)
            stats["total_downvotes"] += post.get("downvotes", 0)
            stats["total_saves"] += post.get("saveCount", 0)
            stats["total_comments"] += post.get("commentCount", 0)

            # 按类型分类
            post_type = post.get("data", {}).get("meta", {}).get("type", "unknown")
            if post_type not in stats["by_type"]:
                stats["by_type"][post_type] = 0
            stats["by_type"][post_type] += 1

            # 单个帖子信息
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
                    "url": f"https://openwebui.com/f/{post.get('slug', '')}",
                }
            )

        # 按下载量排序
        stats["posts"].sort(key=lambda x: x["downloads"], reverse=True)

        return stats

    def print_stats(self, stats: dict):
        """打印统计报告到终端"""
        print("\n" + "=" * 60)
        print("📊 OpenWebUI 社区统计报告")
        print("=" * 60)
        print(f"📅 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # 总览
        print("📈 总览")
        print("-" * 40)
        print(f"  📝 发布数量: {stats['total_posts']}")
        print(f"  ⬇️  总下载量: {stats['total_downloads']}")
        print(f"  👁️  总浏览量: {stats['total_views']}")
        print(f"  👍 总点赞数: {stats['total_upvotes']}")
        print(f"  💾 总收藏数: {stats['total_saves']}")
        print(f"  💬 总评论数: {stats['total_comments']}")
        print()

        # 按类型分类
        print("📂 按类型分类")
        print("-" * 40)
        for post_type, count in stats["by_type"].items():
            print(f"  • {post_type}: {count}")
        print()

        # 详细列表
        print("📋 发布列表 (按下载量排序)")
        print("-" * 60)

        # 表头
        print(f"{'排名':<4} {'标题':<30} {'下载':<8} {'浏览':<8} {'点赞':<6}")
        print("-" * 60)

        for i, post in enumerate(stats["posts"], 1):
            title = (
                post["title"][:28] + ".." if len(post["title"]) > 28 else post["title"]
            )
            print(
                f"{i:<4} {title:<30} {post['downloads']:<8} {post['views']:<8} {post['upvotes']:<6}"
            )

        print("=" * 60)

    def generate_markdown(self, stats: dict) -> str:
        """生成 Markdown 格式报告"""
        md = []
        md.append("# 📊 OpenWebUI 社区统计报告")
        md.append("")
        md.append(f"> 📅 更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append("")

        # 总览
        md.append("## 📈 总览")
        md.append("")
        md.append("| 指标 | 数值 |")
        md.append("|------|------|")
        md.append(f"| 📝 发布数量 | {stats['total_posts']} |")
        md.append(f"| ⬇️ 总下载量 | {stats['total_downloads']} |")
        md.append(f"| 👁️ 总浏览量 | {stats['total_views']} |")
        md.append(f"| 👍 总点赞数 | {stats['total_upvotes']} |")
        md.append(f"| 💾 总收藏数 | {stats['total_saves']} |")
        md.append(f"| 💬 总评论数 | {stats['total_comments']} |")
        md.append("")

        # 按类型分类
        md.append("## 📂 按类型分类")
        md.append("")
        for post_type, count in stats["by_type"].items():
            md.append(f"- **{post_type}**: {count}")
        md.append("")

        # 详细列表
        md.append("## 📋 发布列表")
        md.append("")
        md.append(
            "| 排名 | 标题 | 类型 | 版本 | 下载 | 浏览 | 点赞 | 收藏 | 更新日期 |"
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
        """保存 JSON 格式数据"""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON 数据已保存到: {filepath}")


def main():
    """主函数"""
    # 获取配置
    api_key = os.getenv("OPENWEBUI_API_KEY")
    user_id = os.getenv("OPENWEBUI_USER_ID")

    if not api_key:
        print("❌ 错误: 未设置 OPENWEBUI_API_KEY 环境变量")
        print("请设置环境变量：")
        print("  export OPENWEBUI_API_KEY='your_api_key_here'")
        return EXIT_FAILURE

    # 初始化
    stats_client = OpenWebUIStats(api_key, user_id)
    if not stats_client.user_id:
        print("❌ 错误: 未能获取用户 ID")
        print("请设置环境变量：")
        print("  export OPENWEBUI_USER_ID='your_user_id_here'")
        print("\n提示: 用户 ID 可以从之前的 curl 请求或 Token 中获取")
        print("     例如: b15d1348-4347-42b4-b815-e053342d6cb0")
        return EXIT_FAILURE
    print(f"🔍 用户 ID: {stats_client.user_id}")

    # 获取所有帖子
    print("📥 正在获取帖子数据...")
    posts = stats_client.get_all_posts()
    print(f"✅ 获取到 {len(posts)} 个帖子")

    # 生成统计
    stats = stats_client.generate_stats(posts)

    # 打印到终端
    stats_client.print_stats(stats)

    # 保存 Markdown 报告
    script_dir = Path(__file__).resolve().parent.parent
    output_dir = Path(os.getenv("OPENWEBUI_OUTPUT_DIR", script_dir / "docs"))
    output_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / "community-stats.md"
    md_content = stats_client.generate_markdown(stats)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"\n✅ Markdown 报告已保存到: {md_path}")

    # 保存 JSON 数据
    json_path = output_dir / "community-stats.json"
    stats_client.save_json(stats, str(json_path))

    return EXIT_SUCCESS


if __name__ == "__main__":
    exit(main())
