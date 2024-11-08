THREADS = 5  # 用于注册账户/领取奖励模式/批准邮箱模式的线程数 挖矿的时候不需要设置 几个账号就是几个线程数
MIN_PROXY_SCORE = 50  # 设置为 0 则不检查代理评分（如果网站无法访问）


######################################### 这部分看起来都是验证邮箱和验证钱包
APPROVE_EMAIL = False  # 验证邮箱（需要 IMAP 和邮箱访问权限）
CONNECT_WALLET = False  # 连接钱包（在 wallets.txt 文件中放入私钥）
SEND_WALLET_APPROVE_LINK_TO_EMAIL = False  # 将验证钱包链接发送到邮箱
APPROVE_WALLET_ON_EMAIL = False  # 从邮箱中验证链接（需要 IMAP 和邮箱访问权限）
SEMI_AUTOMATIC_APPROVE_LINK = False  # 如果为 True，则允许手动从邮箱中粘贴批准链接到命令行界面
# 如果可以将所有批准邮件转发到单个 IMAP 地址：
SINGLE_IMAP_ACCOUNT = False  # 使用格式 "name@domain.com:password"

# 自动选择
EMAIL_FOLDER = ""  # 邮件存放的文件夹
IMAP_DOMAIN = ""  # IMAP 域名（并非总能生效）

#########################################
CLAIM_REWARDS_ONLY = False  # 仅领取推荐奖励（https://app.getgrass.io/dashboard/referral-program）

STOP_ACCOUNTS_WHEN_SITE_IS_DOWN = True  # 当网站无法访问时停止账户 20 分钟，以减少代理流量
CHECK_POINTS = False  # 每 10 分钟左右显示一次每个账户的积分
SHOW_LOGS_RARELY = False  # 不总是显示动作信息，以减少对电脑性能的影响

# 挖矿模式
MINING_MODE = True  # False - 不挖掘 grass，True - 挖掘 grass；将所有注册和批准项设置为 False

# 仅注册账户
REGISTER_ACCOUNT_ONLY = False
REGISTER_DELAY = (3, 7)  # 注册时的延迟区间（秒）

TWO_CAPTCHA_API_KEY = ""
ANTICAPTCHA_API_KEY = ""
CAPMONSTER_API_KEY = ""
CAPSOLVER_API_KEY = ""
CAPTCHAAI_API_KEY = ""

# 邮件处理时也使用代理
USE_PROXY_FOR_IMAP = False

# 验证码参数，留空
CAPTCHA_PARAMS = {
    "captcha_type": "v2",
    "invisible_captcha": False,
    "sitekey": "6LeeT-0pAAAAAFJ5JnCpNcbYCBcAerNHlkK4nm6y",
    "captcha_url": "https://app.getgrass.io/register"
}

########################################

ACCOUNTS_FILE_PATH = "data/accounts.txt"
PROXIES_FILE_PATH = "data/proxies.txt"
WALLETS_FILE_PATH = "data/wallets.txt"
