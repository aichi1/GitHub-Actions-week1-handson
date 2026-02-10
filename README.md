# ハンズオン 1: 初めてのGitHub Actionsワークフロー

## 概要

GitHub Actionsで最初のワークフローを作成するハンズオンです。
リポジトリにpushするだけで自動実行される仕組みを体験し、GitHub Actionsの基本的な動作原理を理解します。

## 対応週

Week 1: GitHub Actions基礎

## このハンズオンで学ぶこと

- GitHub Actionsワークフローの基本構造（Workflow, Job, Step）
- `.github/workflows/` ディレクトリの役割
- YAMLファイルによるワークフロー定義
- トリガー（push, pull_request, workflow_dispatch）の設定
- Pythonスクリプトの実行とバージョン表示
- GitHub UI上でのワークフロー実行結果の確認

## 前提条件

- GitHubアカウントを持っている
- Gitの基本操作（clone, commit, push）ができる
- Pythonの基礎を理解している
- テキストエディタ（VS Code推奨）が使える

## サンプルアプリケーション

シンプルな数値計算ツール（`calculator.py`）。四則演算と簡単な統計計算を行うPythonスクリプトです。

## 所要時間目安

約45分〜1時間

## ディレクトリ構成

```
handson-01-first-workflow/
├── README.md              # このファイル
├── instructions/          # 手順書（ステップ別）
│   ├── step-01.md         # リポジトリ作成とファイル配置
│   ├── step-02.md         # 最小構成のワークフロー作成
│   ├── step-03.md         # pushして実行結果を確認
│   ├── step-04.md         # トリガーの追加
│   └── step-05.md         # Pythonスクリプト実行ステップ追加
├── starter/               # 開始時のスケルトンコード
│   ├── src/
│   │   └── calculator.py
│   ├── tests/
│   │   └── test_calculator.py
│   └── pyproject.toml
├── solution/              # 完成版（参考）
│   ├── .github/
│   │   └── workflows/
│   │       └── hello.yml
│   ├── src/
│   │   └── calculator.py
│   ├── tests/
│   │   └── test_calculator.py
│   └── pyproject.toml
└── tips.md                # つまずきポイントと対処法
```

## 進め方

1. `starter/` のファイルをコピーして新しいGitHubリポジトリを作成
2. `instructions/` の手順書を Step 01 から順に進める
3. 各Stepで動作確認を行い、GitHub UIで結果を確認
4. 詰まったら `tips.md` を参照
5. 完成したら `solution/` と見比べて理解を深める
