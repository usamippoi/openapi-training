# OpenAPIのキャッチアップ
【超初心者向け】5分で試せる！OpenAPI(Swagger3.0)ドキュメント作成〜API自動生成
https://qiita.com/se_fy/items/ad05a3c6825bb9612170

# OpenAPI エディター
https://stoplight.io/studio

# プログラム構成v1
repository-top
├── swagger generated controller (import child)
    ├── business logic controller (child)
        ├── basic controller (parent, import log, db)
            ├── log class
            ├── db class
            ├── main process methiod
                ├── start log
                ├── end log

# BigQuery Client の利用例
https://cloud.google.com/blog/ja/products/application-development/inventory-management-bigquery-and-cloud-run

# システム構成v1
Cloud Run
├── Docker
    ├── OpenAPI
        ├── Controller
            ├── BaseController
            ├── API定義
        ├── Models
            ├── BaseModel
                ├── Log
                ├── DB Access
            ├── ビジネスロジック
