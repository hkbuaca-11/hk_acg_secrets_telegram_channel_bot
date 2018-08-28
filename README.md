A fork from [hackernewsbot](https://github.com/phil-r/hackernewsbot) to retrieve and forward new post from Facebook HK ACG-related articles onto [@hk_acg_feeds](https://t.me/hk_acg_feeds) Telegram channel.

Currently this is still in alpha stage of development cycle.

# Statements
## 20180829T064232Z+8
已經 deploy 最新版伺服器程式碼，加入及修復💁‍♂️：
* HKCOS訂服.secrets (fb 2127337204256629)
* Cos3E Secrets.HK (fb 2127337204256629)
* 音ゲーム婊版Hk (fb 318183312053938)
* Maidcafe Secret.HK (fb 213370562463886)
* 增加 m.facebook.com 形式連結供 iOS/Android 等平台直接以 app 方式打開全文
* 調整更新板塊頻率為每 15 分鐘一次


## 20180807T032638Z+8
下一次 deployment 會新增以下各板💁‍♂️：
* Cos3E Secrets.HK (fb 2127337204256629)
* 音ゲーム婊版Hk (fb 318183312053938)
* Maidcafe Secret.HK (fb 213370562463886)

並會將以下項目放入候選之列中🤔：
* 告白香港音Game (fb 163511237462633)
* 匿名香港音Game (fb 1027481327369446)
* 音驚婊白hk (fb 418194352021038)
* HKCOS訂服.secrets (fb 292574281166065)
* acg.secret.2.0 (ig acg.secret.2.0)
* acg.secret.2.5 (ig acg.secret.2.5)
* acgsecret3.0 (ig acgsecret3.0)

亦會修改 Facebook 連結造型，等 iOS/Android 等平台上可以直接用 app 開啟連結。

最近 Facebook 新版 Graph API 使用條款要求開發者嘅程式，每個 Graph API ID 每日應該只能發出 4800 個請求。而本 Telegram 頻道啟用一年以來，各位使用者已經確立係作為備份存檔之用。有見及此，喺下一次 deployment 起，每一個收風點嘅更新頻率會降低到每 15 分鐘一次。
假如各位使用者有特別需要，請考慮自行開發專用程式自行處理。

亦借此 post 脷伸：
本系統 (包括 Facebook Graph API、Google Cloud、Telegram bot、頻道 等) 嘅啟用都係只會收集已經公開嘅資料。並且喺有大量嘅數據嘅時候，希望能夠將內容「餵」俾人工智能 (例如 Natural Language Processing 等)，愛嚟喺未來，可以發展到等相關人士可以有一個更簡便嘅平台，去即時留意同分析整個 ACG(N) 圈入面正在發生嘅事作為目標。

呢個項目嘅最終目標有機會實行唔到，但始終有已經收集到一年份 (純文字，大概 7MB) 。假使有更高能力嘅人士對 NLP 等等有更深入認識的話，呢堆大數據可能會對佢哋有用。

縱使部份開發者有同部份收風點嘅人物有聯系，亦有機會有各項喺 ACG 界上面可稱得上舉足輕重嘅身份，但所有開發者 (目前只有 @soumasandesu ) 並沒有因此對於喺呢個 Telegram 頻道所 (自動) 發佈嘅各項內容，為任何一個人背書。所有內容皆同開發者、原發佈者等等人士嘅立場無關。

而目前開發者人數太少。
如果有任何意見，請去 https://t.me/joinchat/AZtjxk6sSth9SysIrbiduQ 。
如果想自薦幫手開發本項目 (Python, YAML, GAE, Git 等。或會有 Node.js 等)，請喺上面 supergroup 向任一開發者 @ 貼出自己 GitHub profile 並等候回應。

多謝。