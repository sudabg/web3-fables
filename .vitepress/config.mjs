import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Web3 Fables',
  description: 'Learn Web3 concepts through ancient-China-themed allegories',
  base: '/web3-fables/',
  lang: 'zh-CN',
  lastUpdated: true,
  ignoreDeadLinks: true,
  srcExclude: ['README.md', 'scripts/**', 'site/**', 'package.json', 'package-lock.json', 'node_modules/**'],
  themeConfig: {
    logo: '🔮',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Fables', link: '/fables/security/01-the-infinite-borrower' },
      { text: 'Search', link: '/site/search.html' },
      { text: 'GitHub', link: 'https://github.com/sudabg/web3-fables' }
    ],
    sidebar: [
    {
        "text": "🛡️ Security",
        "collapsed": false,
        "items": [
            {
                "text": "无限借贷者",
                "link": "/fables/security/01-the-infinite-borrower"
            },
            {
                "text": "七道门",
                "link": "/fables/security/02-the-seven-gates"
            },
            {
                "text": "伪造的秤",
                "link": "/fables/security/03-the-counterfeit-scale"
            },
            {
                "text": "信使与拍卖行",
                "link": "/fables/security/04-the-messenger-and-the-auction-house"
            },
            {
                "text": "沼泽中的灯塔",
                "link": "/fables/security/05-the-lighthouse-in-the-swamp"
            },
            {
                "text": "风向旗的骗局",
                "link": "/fables/security/06-the-weather-vane-deception"
            }
        ]
    },
    {
        "text": "🏗️ Infrastructure",
        "collapsed": false,
        "items": [
            {
                "text": "影之剧场",
                "link": "/fables/infrastructure/02-the-theater-of-shadows"
            },
            {
                "text": "无钥之城",
                "link": "/fables/infrastructure/03-the-keyless-city"
            },
            {
                "text": "回声工坊",
                "link": "/fables/infrastructure/04-the-factory-of-echoes"
            },
            {
                "text": "雪崩后的账本",
                "link": "/fables/infrastructure/05-the-ledger-after-the-avalanche"
            },
            {
                "text": "压缩商队",
                "link": "/fables/infrastructure/06-the-compressed-caravan"
            },
            {
                "text": "呼吸税",
                "link": "/fables/infrastructure/07-the-breath-tax"
            },
            {
                "text": "桥梁守卫",
                "link": "/fables/infrastructure/08-the-bridge-guard"
            }
        ]
    },
    {
        "text": "💰 DeFi",
        "collapsed": false,
        "items": [
            {
                "text": "自动市集",
                "link": "/fables/defi/01-the-automated-market"
            },
            {
                "text": "锚定之舟",
                "link": "/fables/defi/02-the-anchored-vessel"
            },
            {
                "text": "当铺与保险库",
                "link": "/fables/defi/03-the-pawnshop-and-the-vault"
            },
            {
                "text": "暗巷中的信使",
                "link": "/fables/defi/04-the-messengers-in-the-alley"
            },
            {
                "text": "深井与浅池",
                "link": "/fables/defi/05-the-deep-well-and-the-shallow-pond"
            },
            {
                "text": "分水渠",
                "link": "/fables/defi/06-the-water-dividers"
            },
            {
                "text": "可编程市集",
                "link": "/fables/defi/07-the-programmable-bazaar"
            }
        ]
    },
    {
        "text": "⚙️ EVM",
        "collapsed": false,
        "items": [
            {
                "text": "编号柜",
                "link": "/fables/evm/01-the-numbered-lockers"
            },
            {
                "text": "工匠的工作台",
                "link": "/fables/evm/02-the-craftsmans-workbench"
            },
            {
                "text": "预言家的模具",
                "link": "/fables/evm/03-the-prophets-mold"
            },
            {
                "text": "借身还魂",
                "link": "/fables/evm/04-the-soul-in-borrowed-body"
            },
            {
                "text": "新语法手册",
                "link": "/fables/evm/05-the-new-grammar-manual"
            },
            {
                "text": "传令筒",
                "link": "/fables/evm/06-the-message-tube"
            },
            {
                "text": "符文石",
                "link": "/fables/evm/07-the-runestones"
            }
        ]
    },
    {
        "text": "🔐 Cryptography",
        "collapsed": false,
        "items": [
            {
                "text": "家谱树的证明",
                "link": "/fables/cryptography/01-the-proof-of-the-family-tree"
            },
            {
                "text": "指纹印章",
                "link": "/fables/cryptography/02-the-fingerprint-seal"
            },
            {
                "text": "碎纸机",
                "link": "/fables/cryptography/03-the-shredder"
            },
            {
                "text": "零知识洞穴",
                "link": "/fables/cryptography/04-the-cave-of-zero-knowledge"
            }
        ]
    },
    {
        "text": "🤝 Consensus",
        "collapsed": false,
        "items": [
            {
                "text": "押注者的轮盘",
                "link": "/fables/consensus/01-the-stakers-roulette"
            },
            {
                "text": "失信者的烙印",
                "link": "/fables/consensus/02-the-brand-of-the-faithless"
            },
            {
                "text": "不可撤销的印章",
                "link": "/fables/consensus/03-the-irrevocable-seal"
            }
        ]
    },
    {
        "text": "🏛️ Governance",
        "collapsed": false,
        "items": [
            {
                "text": "冷却室",
                "link": "/fables/governance/01-the-cooling-chamber"
            },
            {
                "text": "砝码民主",
                "link": "/fables/governance/02-the-weighted-democracy"
            }
        ]
    },
    {
        "text": "☀️ Solana",
        "collapsed": false,
        "items": [
            {
                "text": "流水线工坊",
                "link": "/fables/solana/01-the-assembly-line-workshop"
            },
            {
                "text": "铁匠的纪律",
                "link": "/fables/solana/02-the-smiths-discipline"
            },
            {
                "text": "计时保险箱",
                "link": "/fables/solana/03-the-timed-safe"
            },
            {
                "text": "确定性门牌",
                "link": "/fables/solana/04-the-deterministic-address"
            }
        ]
    },
    {
        "text": "📦 Other",
        "collapsed": false,
        "items": [
            {
                "text": "独一无二的令牌",
                "link": "/fables/other/01-the-non-fungible-token"
            },
            {
                "text": "一日借款",
                "link": "/fables/other/02-the-one-day-loan"
            }
        ]
    }
],
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: '搜索寓言',
                buttonAriaLabel: '搜索寓言'
              },
              modal: {
                noResultsText: '未找到相关寓言',
                resetButtonTitle: '清除搜索',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                  closeText: '关闭'
                }
              }
            }
          }
        }
      }
    },
    editLink: {
      pattern: 'https://github.com/sudabg/web3-fables/edit/main/:path',
      text: 'Edit this page on GitHub'
    },
    lastUpdated: {
      text: 'Updated at'
    },
    docFooter: {
      prev: 'Previous Fable',
      next: 'Next Fable'
    }
  },
  head: [
    ['link', { rel: 'icon', href: '/web3-fables/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#66fcf1' }]
  ]
})
