# Rose Lab 幼兒園資料庫｜逐縣市＋逐園 JSON 版

這一版專門用來做到：

- 不改 Rose Lab 文章顯示內容
- 不改既有 `renderSlip()` 資料結構
- 保持原本資料夾邏輯
- GitHub 可逐間園所預覽、編輯
- 不需要手動上傳 1,000+ 個 JSON

## 最終結構

```text
docs/
└── data/
    ├── slip114-index.json
    └── slip114/
        ├── 臺北市/
        │   ├── 某幼兒園.json
        │   └── ...
        ├── 新北市/
        │   ├── 某幼兒園.json
        │   └── ...
        └── ...
```

也就是：

**學年度 → 縣市 → 每間園所一個 JSON**

## 為什麼最適合直接替換文章

目前 Rose Lab 文章引用的是：

```text
https://raw.githubusercontent.com/kiang/ap.ece.moe.edu.tw/refs/heads/master/docs/data/slip114/臺北市/園所名稱.json
```

改成自己的 repo 後，路徑可維持：

```text
https://raw.githubusercontent.com/MIBO2022/rose-lab-kindergarten-data/main/docs/data/slip114/臺北市/園所名稱.json
```

因此後段 `docs/data/slip114/縣市/園所名稱.json` 不變。

文章原本的：

- `renderSlip()`
- `renderClass()`
- tabs
- 學費／雜費／材料費／活動費
- 午餐／點心
- 交通／延托
- 收費期間／單價／小計

都不需要因資料庫而改。

## 第一次執行

1. 把本包內容上傳到：
   `MIBO2022/rose-lab-kindergarten-data`

2. 到 GitHub：
   `Actions`

3. 執行：
   `Build 114 per-school kindergarten database`

4. 按：
   `Run workflow`

5. 完成後 repository 會自動生成：
   `docs/data/slip114/`

## 重要

這個 workflow 會從來源 archive 複製 `slip114` 的逐園 JSON，並保持原始 JSON 內容不變。

網站切換前，先確認至少一間園所新 Raw URL 可以正常開啟，再做文章 URL 前綴替換。
