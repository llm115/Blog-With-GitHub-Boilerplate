# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "师者"
site_logo = "${static_prefix}logo.png"
site_build_date = "2024-2-7T20:21+08:00"
author = "彭彭"
email = "18169hy91@gmail.com"
author_homepage = "https://stellarium-web.org/"
description = "时流若生，生逝如时"
key_words = ['Maverick', '彭彭', 'Campus time', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "There are tears before, but fearless"
    },
    {
        "name": "留档计划",
        "url": "https://drive.google.com/drive/home",
        "brief": "云端"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "",
        "url": "",
        "icon": ""
    },
    {
        "name": "",
        "url": "",
        "icon": ""
    },
    {
        "name": "",
        "url": "",
        "icon": ""
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
