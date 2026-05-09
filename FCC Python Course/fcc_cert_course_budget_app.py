{\rtf1\ansi\ansicpg1252\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red234\green234\blue234;\red0\green0\blue0;
\red144\green1\blue18;\red19\green118\blue70;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c93333\c93333\c93333;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c52549\c34510;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs36 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  math\cb1 \
\cf2 \cb3 \strokec2 class\cf0 \strokec4  Category:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 def\cf0 \strokec4  \cf2 \strokec2 __init__\cf0 \strokec4 (\cf2 \strokec2 self\cf0 \strokec4 , name):\cb1 \
\cb3         \cf2 \strokec2 self\cf0 \strokec4 .name = name\cb1 \
\cb3         \cf2 \strokec2 self\cf0 \strokec4 .ledger = []\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 def\cf0 \strokec4  deposit(\cf2 \strokec2 self\cf0 \strokec4 , amount, description=\cf5 \strokec5 ""\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 self\cf0 \strokec4 .ledger.append(\{\cf5 \strokec5 'amount'\cf0 \strokec4 : amount, \cf5 \strokec5 'description'\cf0 \strokec4 : description\})\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 def\cf0 \strokec4  withdraw(\cf2 \strokec2 self\cf0 \strokec4 , amount, description=\cf5 \strokec5 ""\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 self\cf0 \strokec4 .check_funds(amount) == \cf2 \strokec2 True\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 self\cf0 \strokec4 .ledger.append(\{\cf5 \strokec5 "amount"\cf0 \strokec4 : -amount, \cf5 \strokec5 "description"\cf0 \strokec4 : description\})\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 def\cf0 \strokec4  get_balance(\cf2 \strokec2 self\cf0 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 sum\cf0 \strokec4 (entry[\cf5 \strokec5 "amount"\cf0 \strokec4 ] \cf2 \strokec2 for\cf0 \strokec4  entry \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 self\cf0 \strokec4 .ledger)\cb1 \
\
\cb3     \cf2 \strokec2 def\cf0 \strokec4  transfer(\cf2 \strokec2 self\cf0 \strokec4 , amount, category):\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf2 \strokec2 self\cf0 \strokec4 .check_funds(amount) == \cf2 \strokec2 True\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 self\cf0 \strokec4 .ledger.append(\{\cf5 \strokec5 "amount"\cf0 \strokec4 : -amount, \cf5 \strokec5 "description"\cf0 \strokec4 : \cf5 \strokec5 f"Transfer to \cf0 \strokec4 \{category.name\}\cf5 \strokec5 "\cf0 \strokec4 \})\cb1 \
\cb3             category.ledger.append(\{\cf5 \strokec5 "amount"\cf0 \strokec4 : amount, \cf5 \strokec5 "description"\cf0 \strokec4 : \cf5 \strokec5 f"Transfer from \cf0 \strokec4 \{self.name\}\cf5 \strokec5 "\cf0 \strokec4 \})\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 def\cf0 \strokec4  check_funds(\cf2 \strokec2 self\cf0 \strokec4 , amount):\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  amount > \cf2 \strokec2 self\cf0 \strokec4 .get_balance():\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 def\cf0 \strokec4  __str__(\cf2 \strokec2 self\cf0 \strokec4 ):\cb1 \
\cb3         lines = []\cb1 \
\cb3         lines.append(\cf2 \strokec2 self\cf0 \strokec4 .name.center(\cf6 \strokec6 30\cf0 \strokec4 , \cf5 \strokec5 "*"\cf0 \strokec4 ))\cb1 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  entry \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 self\cf0 \strokec4 .ledger:\cb1 \
\cb3             amount = entry[\cf5 \strokec5 "amount"\cf0 \strokec4 ]\cb1 \
\cb3             description = entry[\cf5 \strokec5 "description"\cf0 \strokec4 ]\cb1 \
\cb3             lines.append(\cf5 \strokec5 f"\cf0 \strokec4 \{description[\cf5 \strokec5 :23]:<23\cf0 \strokec4 \}\{amount\cf5 \strokec5 :>7.2f\cf0 \strokec4 \}\cf5 \strokec5 "\cf0 \strokec4 )\cb1 \
\cb3         lines.append(\cf5 \strokec5 f"Total: \cf0 \strokec4 \{self.get_balance()\cf5 \strokec5 :.2f\cf0 \strokec4 \}\cf5 \strokec5 "\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 "\\n"\cf0 \strokec4 .join(lines)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  create_spend_chart(categories):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     title = \cf5 \strokec5 "Percentage spent by category"\cf0 \cb1 \strokec4 \
\
\cb3     total_spent = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  category \cf2 \strokec2 in\cf0 \strokec4  categories:\cb1 \
\cb3         category_total_spent = \cf2 \strokec2 sum\cf0 \strokec4 (entry[\cf5 \strokec5 "amount"\cf0 \strokec4 ] \cf2 \strokec2 for\cf0 \strokec4  entry \cf2 \strokec2 in\cf0 \strokec4  category.ledger \cf2 \strokec2 if\cf0 \strokec4  entry[\cf5 \strokec5 "amount"\cf0 \strokec4 ] < \cf6 \strokec6 0\cf0 \strokec4 )\cb1 \
\cb3         total_spent.append(category_total_spent)\cb1 \
\cb3     overall_total = \cf2 \strokec2 sum\cf0 \strokec4 (total_spent)\cb1 \
\
\cb3     percentages = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  spent \cf2 \strokec2 in\cf0 \strokec4  total_spent:\cb1 \
\cb3         pct = math.floor((\cf2 \strokec2 abs\cf0 \strokec4 (spent)/ \cf2 \strokec2 abs\cf0 \strokec4 (overall_total)) * \cf6 \strokec6 100\cf0 \strokec4  / \cf6 \strokec6 10\cf0 \strokec4 ) * \cf6 \strokec6 10\cf0 \cb1 \strokec4 \
\cb3         percentages.append(pct)\cb1 \
\
\cb3     lines = []\cb1 \
\cb3     lines.append(title)\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  i \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (\cf6 \strokec6 100\cf0 \strokec4 , \cf6 \strokec6 -1\cf0 \strokec4 , \cf6 \strokec6 -10\cf0 \strokec4 ):\cb1 \
\cb3         row = \cf5 \strokec5 f"\cf0 \strokec4 \{i\cf5 \strokec5 :>3\cf0 \strokec4 \}\cf5 \strokec5 |"\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  pct \cf2 \strokec2 in\cf0 \strokec4  percentages:\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  pct >= i:\cb1 \
\cb3                 row += \cf5 \strokec5 " o "\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 row += \cf5 \strokec5 "   "\cf0 \cb1 \strokec4 \
\cb3         row += \cf5 \strokec5 " "\cf0 \cb1 \strokec4 \
\cb3         lines.append(row)\cb1 \
\cb3     lines.append(\cf5 \strokec5 "    "\cf0 \strokec4  + \cf5 \strokec5 "-"\cf0 \strokec4  * (\cf2 \strokec2 len\cf0 \strokec4 (categories) * \cf6 \strokec6 3\cf0 \strokec4  + \cf6 \strokec6 1\cf0 \strokec4 ))\cb1 \
\cb3     \cf2 \strokec2 print\cf0 \strokec4 (total_spent)\cb1 \
\cb3     \cf2 \strokec2 print\cf0 \strokec4 (overall_total)\cb1 \
\cb3     \cf2 \strokec2 print\cf0 \strokec4 (percentages)\cb1 \
\
\cb3     max_len = \cf2 \strokec2 max\cf0 \strokec4 (\cf2 \strokec2 len\cf0 \strokec4 (category.name) \cf2 \strokec2 for\cf0 \strokec4  category \cf2 \strokec2 in\cf0 \strokec4  categories)\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  i \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 range\cf0 \strokec4 (max_len):\cb1 \
\cb3         row = \cf5 \strokec5 "     "\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 for\cf0 \strokec4  category \cf2 \strokec2 in\cf0 \strokec4  categories:\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  i < \cf2 \strokec2 len\cf0 \strokec4 (category.name):\cb1 \
\cb3                 row += category.name[i] + \cf5 \strokec5 "  "\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 row += \cf5 \strokec5 "   "\cf0 \cb1 \strokec4 \
\cb3         lines.append(row)\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf5 \strokec5 '\\n'\cf0 \strokec4 .join(lines)\cb1 \
\
\
\cb3 food = Category(\cf5 \strokec5 'Food'\cf0 \strokec4 )\cb1 \
\cb3 food.deposit(\cf6 \strokec6 1000\cf0 \strokec4 , \cf5 \strokec5 'initial deposit'\cf0 \strokec4 )\cb1 \
\cb3 food.withdraw(\cf6 \strokec6 10.15\cf0 \strokec4 , \cf5 \strokec5 'groceries'\cf0 \strokec4 )\cb1 \
\cb3 food.withdraw(\cf6 \strokec6 15.89\cf0 \strokec4 , \cf5 \strokec5 'restaurant and more food for dessert'\cf0 \strokec4 )\cb1 \
\cb3 clothing = Category(\cf5 \strokec5 'Clothing'\cf0 \strokec4 )\cb1 \
\cb3 food.transfer(\cf6 \strokec6 50\cf0 \strokec4 , clothing)\cb1 \
\cb3 auto = Category(\cf5 \strokec5 'Auto'\cf0 \strokec4 )\cb1 \
\cb3 auto.deposit(\cf6 \strokec6 1000\cf0 \strokec4 )\cb1 \
\cb3 auto.withdraw(\cf6 \strokec6 33.40\cf0 \strokec4 , \cf5 \strokec5 'fuel'\cf0 \strokec4 )\cb1 \
\cb3 auto.withdraw(\cf6 \strokec6 100\cf0 \strokec4 , \cf5 \strokec5 'repairs'\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 print\cf0 \strokec4 (create_spend_chart([food, clothing, auto]))\cb1 \
\
}