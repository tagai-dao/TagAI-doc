#!/usr/bin/env python3
"""
从 GitBook 公开站点拉取各页 .md 源文件，写入 docs/ 下**中文路径**（与 mkdocs.yml 一致）。
仅作同步更新时使用；平时直接编辑 docs/ 即可。
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = "https://coincidence-labs.gitbook.io/tagai"
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# GitBook URL 路径段 → 仓库内相对 docs/ 的路径（含 .md）
GITBOOK_TO_LOCAL: dict[str, str] = {
    # 首页：写入中文正文文件；index.md 仅 include，勿覆盖为全文
    "readme": "TagAI是什么.md",
    "01-kai-shi-shi-yong/deng-lu-yu-qian-bao-chuang-jian": "开始使用/登录与钱包创建.md",
    "01-kai-shi-shi-yong/jin-xing-ni-de-di-yi-ci-jiao-yi": "开始使用/进行你的第一次交易.md",
    "01-kai-shi-shi-yong/ru-he-cun-kuan": "开始使用/如何存款.md",
    "02-chuang-jian-yu-ce-shi-chang-yu-ti-gong-liu-dong-xing/chuang-jian-she-jiao-yu-ce": "创建预测市场与提供流动性/创建社交预测.md",
    "02-chuang-jian-yu-ce-shi-chang-yu-ti-gong-liu-dong-xing/zuo-shi-shang-ru-he-ti-gong-liu-dong-xing": "创建预测市场与提供流动性/做市商如何提供流动性.md",
    "03-shi-chang-yu-jiao-yi/jia-ge-ru-he-ji-suan": "市场与交易/价格如何计算.md",
    "03-shi-chang-yu-jiao-yi/shi-chang-ru-he-xing-cheng": "市场与交易/市场如何形成.md",
    "04-yu-ce-shen-me-ji-jie-guo-jie-suan/yu-ce-shen-me": "预测什么及结果结算/预测什么.md",
    "04-yu-ce-shen-me-ji-jie-guo-jie-suan/jie-guo-jie-suan-yu-dui-huan": "预测什么及结果结算/结果结算与兑换.md",
    "05-she-jiao-yu-ce-shi-chang/bei-jing": "社交预测市场/背景.md",
    "05-she-jiao-yu-ce-shi-chang/she-qu-qu-dong-de-yu-ce-shi-chang": "社交预测市场/社区驱动的预测市场.md",
    "05-she-jiao-yu-ce-shi-chang/she-jiao-yu-yan-ji": "社交预测市场/社交预言机.md",
    "05-she-jiao-yu-ce-shi-chang/ji-yu-she-qu-gong-shi-de-shi-jian-jie-suan": "社交预测市场/基于社区共识的事件结算.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/she-jiao-fen-fa-yu-web2-cai-yong": "社交分发与Web2采用/社交分发与web2采用.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/cao-zuo-zhi-nan-she-jiao-fen-fa-ji-jiao-yi": "社交分发与Web2采用/操作指南-社交分发及交易.md",
    "07-lian-xi-wo-men/bnb-chain": "联系我们/BNB链.md",
    "07-lian-xi-wo-men/lian-xi-wo-men": "联系我们/联系我们.md",
    "05-she-jiao-yu-ce-shi-chang/she-jiao-yu-yan-ji/jian-rong-web2-de-web3-she-jiao-zhang-hu": "社交预测市场/社交预言机/兼容web2的web3社交账户.md",
    "05-she-jiao-yu-ce-shi-chang/she-jiao-yu-yan-ji/she-jiao-yu-yan-ji-tong-bu-she-jiao-shu-ju": "社交预测市场/社交预言机/社交预言机同步社交数据.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/cao-zuo-zhi-nan-she-jiao-fen-fa-ji-jiao-yi/kai-tong-web3-she-jiao-zhang-hu": "社交分发与Web2采用/操作指南-社交分发及交易/开通Web3社交账户.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/cao-zuo-zhi-nan-she-jiao-fen-fa-ji-jiao-yi/chuang-zuo-yu-zhi-ya-shi-ce-zhan": "社交分发与Web2采用/操作指南-社交分发及交易/创作与质押式策展.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/cao-zuo-zhi-nan-she-jiao-fen-fa-ji-jiao-yi/shen-ling-jiang-li-yu-jiao-yi-dai-bi": "社交分发与Web2采用/操作指南-社交分发及交易/申领奖励与交易代币.md",
    "06-she-jiao-fen-fa-yu-web2-cai-yong/cao-zuo-zhi-nan-she-jiao-fen-fa-ji-jiao-yi/tagai-si-yao-dao-ru-qi-ta-qian-bao-okx-qian-bao-wei-li-zhi-nan": "社交分发与Web2采用/操作指南-社交分发及交易/TagAI私钥导入其他钱包（OKX钱包为例）指南.md",
}


def curl_get(url: str) -> str:
    r = subprocess.run(
        ["curl", "-fsSL", url],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if r.returncode != 0:
        print(f"FAIL {url}: {r.stderr}", file=sys.stderr)
        sys.exit(1)
    return r.stdout


def normalize_md(text: str) -> str:
    return text.replace("&#x26;", "&")


def write_file(rel: Path, body: str) -> None:
    path = DOCS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalize_md(body), encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    for remote, local in GITBOOK_TO_LOCAL.items():
        url = f"{BASE}/{remote}.md" if remote != "readme" else f"{BASE}/readme.md"
        body = curl_get(url)
        write_file(Path(local), body)
    print(
        "提示：已更新 TagAI是什么.md；index.md 仍为 include 桩，请勿用 GitBook 全文覆盖 index.md。",
        file=sys.stderr,
    )
    print("done.")


if __name__ == "__main__":
    main()
