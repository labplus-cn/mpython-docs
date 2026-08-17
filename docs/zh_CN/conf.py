import sys
import os
import datetime
sys.path.insert(0, os.path.abspath('..'))
from conf_common import *  

project = u'mPython掌控'
copyright = u'2018-{year} labplus.All Rights Reserved'.format(year=datetime.datetime.now().year)
author = u'tangliufeng'

language = 'zh_CN'
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
\usepackage{xeCJK}
\setCJKmainfont[BoldFont=STZhongsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\parindent 2em
\definecolor{VerbatimColor}{rgb}{0.95,0.95,0.95}
\setcounter{tocdepth}{3}
\renewcommand\familydefault{\ttdefault}
\renewcommand\CJKfamilydefault{\CJKrmdefault}
'''
}
# 设置文档
latex_documents = [
    (master_doc, 'mpython.tex', 'mpython',
     'labplus', 'manual', True),
]