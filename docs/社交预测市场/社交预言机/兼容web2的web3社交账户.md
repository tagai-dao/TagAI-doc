# 兼容 web2 的 web3 社交账户

#### Web2 社交平台与社交协议组合

Farcaster DApp 的核心定位由”加密原生的社交媒体平台“向”钱包“的转向，让我们看到了：我们可以通过一系列社交中间件，将 web2 社交媒体平台与 Steem、Farcaster 这样的去中心化社交协议进行组合，而非从一开始就仅构建加密原生的社交 DApp。

社交媒体网络的注意力与区块链网络的流动性进行融合的过程，可以基于原有的 web2 社交媒体平台的注意力池，而非新造一个个注意力池。2020年，我们看到：DeFi 的爆发式增长，从 Chainlink 价格预言机 —— 将链外价格引入链上 —— 构建 OK 开始。

于是，我们非常认可 vitalik 的提议 —— 开发者可以围绕 X 等社媒开发替代客户端。其第一步，就是创造一套兼容 web2 社交账号登录，并支持用户在 web2 社交平台创作 & 社交互动，社交数据同步 & 存储在社交协议的系统<sup>\[11]</sup> 。

#### We3 社交账户

TagAI 内置 Privy 钱包，人们可以直接社交媒体账号（比如 X）或邮箱授权登录，并自动创建钱包地址。

进一步，TagAI 与 Steem 区块链组合<sup>\[12]</sup>。TagAI 上已创建钱包地址的账户，只需支付基本注册费用（0.001 $BNB），即可由用户钱包签名生成其 web3 社交账户。

<figure><img src="https://3381154666-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5W3YHzppdMaC2HCthnq8%2Fuploads%2FBI4NdP6bDXPp29aX2YE8%2F634.png?alt=media&token=9e847af5-ab86-41ae-b7f5-8cff9cd049a7" alt=""><figcaption></figcaption></figure>

#### 社交授权及代理资源费用

用户在签名生成 web3 社交账户时，该账户的社交操作权限同步授权给 TagAI。这使用了 Steem 区块链的分层账号体系和账号授权的能力。

<figure><img src="https://3381154666-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5W3YHzppdMaC2HCthnq8%2Fuploads%2Fml2OlSDyieKaN0FzBupb%2F446.png?alt=media&token=e58aa10a-727c-4ef9-a194-ae3e3a05e228" alt=""><figcaption></figcaption></figure>

TagAI 的社交授权服务，不仅让使用 TagAI 签名生成的 web3 社交账户可以对 TagAI 授权社交权限，还支持其对 TagAI 生态 DApp 授权社交权限。

TagAI 也会同步代理资源使用费用给到该账户。如下图，TagAI 对每一个创建的 web3 社交账户代理至少 3 $SP<sup>\[13]</sup>，以使创建的 web3 社交账户可以在社交 DA 进行日常操作。

<figure><img src="https://3381154666-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5W3YHzppdMaC2HCthnq8%2Fuploads%2FQMD59ucPu7bAEIEK9NnI%2F946.png?alt=media&token=23458f8d-fbe9-421b-9fe5-90cd8edfe1d8" alt=""><figcaption></figcaption></figure>

\[11] TagAI 的这一系列社交中间件由 Wormhole3 提供支持

\[12] Steem 区块链作为社交专有区块链，拥有极高的性能，且对短名称设计、社交等权限授权、代理资源费用、第三方代理生成账号等进行了详细考虑。这使得它能够作为社交 DA，可信 &低成本地与智能合约链进行组合。

\[13] 代理的 3 $SP 其所有权属于 TagAI，用户持有 $SP 可以支付资源使用的费用，但无法对此进行解质押、赎回等操作。
