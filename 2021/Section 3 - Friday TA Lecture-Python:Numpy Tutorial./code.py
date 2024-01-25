{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Agenda\n",
    "\n",
    "1. Installation\n",
    "\n",
    "2. Basics\n",
    "\n",
    "3. Iterables \n",
    "\n",
    "4. Numpy (for math and matrix operations)\n",
    "\n",
    "5. Matplotlib (for plotting)\n",
    "\n",
    "6. Q&A "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Note: This tutorial is based on Python 3.8\n",
    "#       but it should apply to all Python 3.X versions\n",
    "# Please note that this tutorial is NOT exhaustive\n",
    "# We try to cover everything you need for class assignments\n",
    "# but you should also navigate external resources\n",
    "#\n",
    "# More tutorials:\n",
    "# NUMPY:\n",
    "# https://cs231n.github.io/python-numpy-tutorial/#numpy\n",
    "# https://numpy.org/doc/stable/user/quickstart.html\n",
    "# MATPLOTLIB:\n",
    "# https://matplotlib.org/gallery/index.html\n",
    "# BASICS:\n",
    "# https://www.w3schools.com/python/\n",
    "# CONSULT THESE WISELY:\n",
    "# The official documentation, Google, and Stack-overflow are your friends!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Installation\n",
    "#### Anaconda for environment management \n",
    "\n",
    "https://www.anaconda.com/\n",
    "\n",
    "common commands\n",
    "\n",
    "conda env list                                <-- list all environments\n",
    "\n",
    "conda create -n newenv python=3.8            <-- create new environment\n",
    "\n",
    "conda enc create -f env.yml     <-- create environment from config file\n",
    "\n",
    "conda activate envname                       <-- activate a environment\n",
    "\n",
    "conda deactivate                                   <-- exit environment\n",
    "\n",
    "pip install packagename     <-- install package for current environment\n",
    "\n",
    "jupyter notebook                <-- open jupyter in current environment\n",
    "\n",
    "#### Package installation using conda/pip\n",
    "Live demo\n",
    "#### Recommended IDEs\n",
    "Spyder (in-built in Anaconda) <br/>\n",
    "Pycharm (the most popular choice, compatible with Anaconda)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [],
   "source": [
    "# common anaconda commands\n",
    "#conda env list\n",
    "#conda create -n name python=3.8\n",
    "#conda env create -f env.yml\n",
    "#conda activate python2.7\n",
    "#conda deactivate\n",
    "#install packages\n",
    "#pip install <package>       "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Basics\n",
    "\n",
    "https://www.w3schools.com/python/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cs229\n",
      "hello, cs229\n"
     ]
    }
   ],
   "source": [
    "# input and output\n",
    "name = input()\n",
    "print(\"hello, \" + name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "print with new line\n",
      "print without new line\n",
      "print multiple variables separated by a space: cs229 1 3.0 True\n"
     ]
    }
   ],
   "source": [
    "print(\"print with new line\")\n",
    "print(\"print without new line\", end=\"\")\n",
    "print()\n",
    "print(\"print multiple variables separated by a space:\", name, 1, 3.0, True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nblock \\ncomments\\n'"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# line comment\n",
    "\"\"\"\n",
    "block \n",
    "comments\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [],
   "source": [
    "# variables don't need explicit declaration\n",
    "var = \"hello\" # string\n",
    "var = 10.0    # float\n",
    "var = 10      # int\n",
    "var = True    # boolean\n",
    "var = [1,2,3] # pointer to list\n",
    "var = None    # empty pointer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "10\n",
      "10.0\n"
     ]
    }
   ],
   "source": [
    "# type conversions\n",
    "var = 10\n",
    "print(int(var))\n",
    "print(str(var))\n",
    "print(float(var))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "var + 4 = 14\n",
      "var - 4 = 6\n",
      "var * 4 = 40\n",
      "var ^ 4= 10000\n",
      "int(var) / 4 = 2\n",
      "float(var) / 4 = 2.5\n"
     ]
    }
   ],
   "source": [
    "# basic math operations\n",
    "var = 10\n",
    "print(\"var + 4 =\", 10 + 4)\n",
    "print(\"var - 4 =\", 10 - 4)\n",
    "print(\"var * 4 =\", 10 * 4)\n",
    "print(\"var ^ 4=\", 10 ** 4)\n",
    "print(\"int(var) / 4 =\", 10//4)   # // for int division\n",
    "print(\"float(var) / 4 =\", 10/4)  # / for float division\n",
    "# All compound assignment operators available\n",
    "# including += -= *= **= /= //= \n",
    "# pre/post in/decrementers not available (++ --)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not True is False\n",
      "True and False is False\n",
      "True or False is True\n"
     ]
    }
   ],
   "source": [
    "# basic boolean operations include \"and\", \"or\", \"not\"\n",
    "print(\"not True is\", not True)\n",
    "print(\"True and False is\", True and False)\n",
    "print(\"True or False is\", True or False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "S\n",
      "tr\n",
      "This is a String!\n",
      "string\n",
      "StringStringStringString\n",
      "True\n",
      "2\n",
      "['I', 'am', 'a', 'sentence']\n",
      "a...b...c\n",
      "Formatting a string like 0.12\n",
      "Or like String!\n"
     ]
    }
   ],
   "source": [
    "# String operations\n",
    "# '' and \"\" are equivalent\n",
    "s = \"String\"\n",
    "#s = 'Mary said \"Hello\" to John'\n",
    "#s = \"Mary said \\\"Hello\\\" to John\"\n",
    "\n",
    "# basic\n",
    "print(len(s)) # get length of string and any iterable type\n",
    "print(s[0]) # get char by index\n",
    "print(s[1:3]) # [1,3)\n",
    "print(\"This is a \" + s + \"!\")\n",
    "\n",
    "# handy tools\n",
    "print(s.lower())\n",
    "print(s*4)\n",
    "print(\"ring\" in s)\n",
    "print(s.index(\"ring\"))\n",
    "\n",
    "# slice by delimiter\n",
    "print(\"I am a sentence\".split(\" \"))\n",
    "# concatenate a list of string using a delimiter\n",
    "print(\"...\".join(['a','b','c']))\n",
    "\n",
    "# formatting variables\n",
    "print(\"Formatting a string like %.2f\"%(0.12345)) \n",
    "print(f\"Or like {s}!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "outer loop\n",
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "outer loop\n",
      "inner loop\n",
      "inner loop\n",
      "inner loop\n",
      "outer loop\n",
      "inner loop\n",
      "inner loop\n",
      "outer loop\n",
      "inner loop\n",
      "outer loop\n"
     ]
    }
   ],
   "source": [
    "# control flows\n",
    "# NOTE: No parentheses or curly braces\n",
    "#       Indentation is used to identify code blocks\n",
    "#       So never ever mix spaces with tabs\n",
    "for i in range(0,5):\n",
    "    for j in range(i, 5):\n",
    "        print(\"inner loop\")\n",
    "    print(\"outer loop\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=\n"
     ]
    }
   ],
   "source": [
    "# if-else\n",
    "var = 10\n",
    "if var > 10:\n",
    "    print(\">\")\n",
    "elif var == 10:\n",
    "    print(\"=\")\n",
    "else:\n",
    "    print(\"<\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "object\n"
     ]
    }
   ],
   "source": [
    "# use \"if\" to check null pointer or empty arrays\n",
    "var = None\n",
    "if var: \n",
    "    print(var)\n",
    "var = []\n",
    "if var:\n",
    "    print(var)\n",
    "var = \"object\"\n",
    "if var:\n",
    "    print(var)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# while-loop\n",
    "var = 5\n",
    "while var > 0:\n",
    "    print(var)\n",
    "    var -=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "-------\n",
      "2\n",
      "0\n",
      "-2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'\\nequivalent to\\nfor (int i = 2; i > -3; i-=2)\\n'"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# for-loop\n",
    "for i in range(3):  # prints 0 1 2\n",
    "    print(i)\n",
    "    \n",
    "\"\"\"\n",
    "equivalent to\n",
    "for (int i = 0; i < 3; i++)\n",
    "\"\"\"\n",
    "print(\"-------\")\n",
    "# range (start-inclusive, stop-exclusive, step)\n",
    "for i in range(2, -3, -2): \n",
    "    print(i)\n",
    "\"\"\"\n",
    "equivalent to\n",
    "for (int i = 2; i > -3; i-=2)\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# define function\n",
    "def func(a, b):\n",
    "    return a + b\n",
    "func(1,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# use default parameters and pass values by parameter name\n",
    "def rangeCheck(a, min_val = 0, max_val=10):\n",
    "    return min_val < a < max_val    # syntactic sugar\n",
    "rangeCheck(5, max_val=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "# define class\n",
    "class Foo:\n",
    "    \n",
    "    # optinal constructor\n",
    "    def __init__(self, x):\n",
    "        # first parameter \"self\" for instance reference, like \"this\" in JAVA\n",
    "        self.x = x\n",
    "    \n",
    "    # instance method\n",
    "    def printX(self): # instance reference is required for all function parameters\n",
    "        print(self.x)\n",
    "        \n",
    "    # class methods, most likely you will never need this\n",
    "    @classmethod\n",
    "    def printHello(self):\n",
    "        print(\"hello\")\n",
    "        \n",
    "obj = Foo(6)\n",
    "obj.printX()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# class inheritance - inherits variables and methods\n",
    "# You might need this when you learn more PyTorch\n",
    "class Bar(Foo):\n",
    "    pass\n",
    "obj = Bar(3)\n",
    "obj.printX()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Iterables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "alist = list()  # linear, size not fixed, not hashable\n",
    "atuple = tuple() # linear, fixed size, hashable\n",
    "adict = dict()  # hash table, not hashable, stores (key,value) pairs\n",
    "aset = set()    # hash table, like dict but only stores keys\n",
    "acopy = alist.copy() # shallow copy\n",
    "print(len(alist)) # gets size of any iterable type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'list'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-182-47597361a541>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0md\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0md\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"a\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"cat\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0md\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"a\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"cat\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m11\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'list'"
     ]
    }
   ],
   "source": [
    "# examplar tuple usage\n",
    "# creating a dictionary to store ngram counts\n",
    "d = dict()\n",
    "d[(\"a\",\"cat\")] = 10\n",
    "d[[\"a\",\"cat\"]] = 11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "[5, 2, 3, 4, 5]\n",
      "----------\n",
      "5\n",
      "4\n",
      "[4, 5]\n",
      "[5, 2, 3]\n",
      "[3, 4]\n",
      "[]\n",
      "[5, 4, 3, 2, 5]\n",
      "----------\n",
      "[2, 3, 4, 5, 'new item', 2, 3, 4]\n",
      "----------\n",
      "found\n",
      "----------\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "new item\n",
      "2\n",
      "3\n",
      "4\n",
      "----------\n",
      "0 2\n",
      "1 3\n",
      "2 4\n",
      "3 5\n",
      "4 new item\n",
      "5 2\n",
      "6 3\n",
      "7 4\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "List: not hashable (i.e. can't use as dictionary key)\n",
    "      dynamic size\n",
    "      allows duplicates and inconsistent element types\n",
    "      dynamic array implementation\n",
    "\"\"\"\n",
    "# list creation\n",
    "alist = []          # empty list, equivalent to list()\n",
    "alist = [1,2,3,4,5] # initialized list\n",
    "\n",
    "print(alist[0])\n",
    "alist[0] = 5\n",
    "print(alist)\n",
    "\n",
    "print(\"-\"*10)\n",
    "# list indexing\n",
    "print(alist[0]) # get first element (at index 0)\n",
    "print(alist[-2]) # get last element (at index len-1)\n",
    "print(alist[3:]) # get elements starting from index 3 (inclusive)\n",
    "print(alist[:3]) # get elements stopping at index 3 (exclusive)\n",
    "print(alist[2:4]) # get elements within index range [2,4)\n",
    "print(alist[6:]) # prints nothing because index is out of range\n",
    "print(alist[::-1]) # returns a reversed list\n",
    "\n",
    "print(\"-\"*10)\n",
    "# list modification\n",
    "alist.append(\"new item\") # insert at end\n",
    "alist.insert(0, \"new item\") # insert at index 0\n",
    "alist.extend([2,3,4]) # concatenate lists\n",
    "# above line is equivalent to alist += [2,3,4]\n",
    "alist.index(\"new item\") # search by content\n",
    "alist.remove(\"new item\") # remove by content\n",
    "alist.pop(0) # remove by index\n",
    "print(alist)\n",
    "\n",
    "print(\"-\"*10)\n",
    "if \"new item\" in alist:\n",
    "    print(\"found\")\n",
    "else:\n",
    "    print(\"not found\")\n",
    "\n",
    "print(\"-\"*10)\n",
    "# list traversal\n",
    "for ele in alist:\n",
    "    print(ele)\n",
    "\n",
    "print(\"-\"*10)\n",
    "# or traverse with index\n",
    "for i, ele in enumerate(alist):\n",
    "    print(i, ele)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Tuple: hashable (i.e. can use as dictionary key)\n",
    "       fixed size (no insertion or deletion)\n",
    "\"\"\"\n",
    "# it does not make sense to create empty tuples\n",
    "atuple = (1,2,3,4,5) \n",
    " # or you can cast other iterables to tuple\n",
    "atuple = tuple([1,2,3])\n",
    "\n",
    "# indexing and traversal are same as list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0 5.0\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Named tuples for readibility\n",
    "\"\"\"\n",
    "from collections import namedtuple\n",
    "Point = namedtuple('Point', 'x y')\n",
    "pt1 = Point(1.0, 5.0)\n",
    "pt2 = Point(2.5, 1.5)\n",
    "print(pt1.x, pt1.y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'a': 1, 'b': 2, 'c': 3}\n",
      "dict_keys(['a', 'b', 'c'])\n",
      "1\n",
      "----------\n",
      "a 1\n",
      "b 2\n",
      "c 3\n",
      "e 5\n",
      "----------\n",
      "a 1\n",
      "b 2\n",
      "c 3\n",
      "e 5\n",
      "----------\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Dict: not hashable \n",
    "      dynamic size\n",
    "      no duplicates allowed\n",
    "      hash table implementation which is fast for searching\n",
    "\"\"\"\n",
    "# dict creation\n",
    "adict = {} # empty dict, equivalent to dict()\n",
    "adict = {'a':1, 'b':2, 'c':3}\n",
    "print(adict)\n",
    "\n",
    "# get all keys in dictionary\n",
    "print(adict.keys())\n",
    "\n",
    "# get value paired with key\n",
    "print(adict['a'])\n",
    "key = 'e'\n",
    "\n",
    "# NOTE: accessing keys not in the dictionary leads to exception\n",
    "if key in adict:\n",
    "    print(adict[key])\n",
    "    \n",
    "# add or modify dictionary entries\n",
    "adict['e'] = 10 # insert new key\n",
    "adict['e'] = 5  # modify existing keys\n",
    "\n",
    "print(\"-\"*10)\n",
    "# traverse keys only\n",
    "for key in adict:\n",
    "    print(key, adict[key])\n",
    "\n",
    "print(\"-\"*10)\n",
    "# or traverse key-value pairs together\n",
    "for key, value in adict.items():\n",
    "    print(key, value)\n",
    "\n",
    "print(\"-\"*10)\n",
    "# NOTE: Checking if a key exists\n",
    "key = 'e'\n",
    "if key in adict: # NO .keys() here please!\n",
    "    print(adict[key])\n",
    "else:\n",
    "    print(\"Not found!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4]\n",
      "feline\n",
      "unknown\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Special dictionaries \n",
    "\"\"\"\n",
    "# set is a dictionary without values\n",
    "aset = set()\n",
    "aset.add('a')\n",
    "\n",
    "# deduplication short-cut using set\n",
    "alist = [1,2,3,3,3,4,3]\n",
    "alist = list(set(alist))\n",
    "print(alist)\n",
    "\n",
    "# default_dictionary returns a value computed from a default function\n",
    "#     for non-existent entries\n",
    "from collections import defaultdict\n",
    "adict = defaultdict(lambda: 'unknown')\n",
    "adict['cat'] = 'feline'\n",
    "print(adict['cat'])\n",
    "print(adict['dog'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'t': 11, 'e': 1})\n",
      "----------\n",
      "Counter({'e': 4, 't': 4, ' ': 3, 'o': 2, 'l': 1, 'r': 1, 's': 1, 'b': 1, 'c': 1, 'u': 1, 'n': 1, 'd': 1})\n",
      "----------\n",
      "1 Counter({'t': 15, 'e': 5, ' ': 3, 'o': 2, 'l': 1, 'r': 1, 's': 1, 'b': 1, 'c': 1, 'u': 1, 'n': 1, 'd': 1})\n",
      "2, Counter({'t': 7})\n",
      "3 Counter({'t': 11, 'e': 1})\n"
     ]
    }
   ],
   "source": [
    "# counter is a dictionary with default value of 0\n",
    "#     and provides handy iterable counting tools\n",
    "from collections import Counter\n",
    "\n",
    "# initialize and modify empty counter\n",
    "counter1 = Counter()\n",
    "counter1['t'] = 10\n",
    "counter1['t'] += 1\n",
    "counter1['e'] += 1\n",
    "print(counter1)\n",
    "print(\"-\"*10)\n",
    "\n",
    "# initialize counter from iterable\n",
    "counter2 = Counter(\"letters to be counted\")\n",
    "print(counter2)\n",
    "print(\"-\"*10)\n",
    "\n",
    "# computations using counters\n",
    "print(\"1\", counter1 + counter2)\n",
    "print(\"2,\", counter1 - counter2)\n",
    "print(\"3\", counter1 or counter2) # or for intersection, and for union"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 1, 4, 5, 6, 7, 8, 9]\n",
      "[9, 8, 7, 6, 5, 4, 1, 1, 0]\n"
     ]
    }
   ],
   "source": [
    "# sorting\n",
    "a = [4,6,1,7,0,5,1,8,9]\n",
    "a = sorted(a)\n",
    "print(a)\n",
    "a = sorted(a, reverse=True)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('bird', 2), ('cat', 1), ('dog', 3)]\n",
      "[('cat', 1), ('bird', 2), ('dog', 3)]\n"
     ]
    }
   ],
   "source": [
    "# sorting\n",
    "a = [(\"cat\",1), (\"dog\", 3), (\"bird\", 2)]\n",
    "a = sorted(a)\n",
    "print(a)\n",
    "a = sorted(a, key=lambda x:x[1])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('bird', 1), ('cat', 3)]\n"
     ]
    }
   ],
   "source": [
    "# useful in dictionary sorting\n",
    "adict = {'cat':3, 'bird':1}\n",
    "print(sorted(adict.items(), key=lambda x:x[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 11, 14, 20, 14]\n",
      "[8, 11]\n"
     ]
    }
   ],
   "source": [
    "# Syntax sugar: one-line control flow + list operation\n",
    "x = [1,2,3,5,3]\n",
    "\"\"\"\n",
    "for i in range(len(sent)):\n",
    "    sent[i] = sent[i].lower().split(\" \")\n",
    "\"\"\" \n",
    "x1 = [xx*3 + 5 for xx in x]\n",
    "print(x1)\n",
    "\n",
    "x2 = [xx*3 + 5 for xx in x if xx < 3]\n",
    "print(x2)\n",
    "\n",
    "# Use this for deep copy!\n",
    "# copy = [obj.copy() for obj in original]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------\n",
      "[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n",
      "[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]\n",
      "[[1], [], [], [], [], [], [], [], [], []]\n"
     ]
    }
   ],
   "source": [
    "# Syntax sugar: * operator for repeating iterable elements\n",
    "print(\"-\"*10)\n",
    "print([1]*10)\n",
    "\n",
    "# Note: This only repeating by value\n",
    "#       So you cannot apply the trick on reference types\n",
    "\n",
    "# To create a double list\n",
    "# DONT\n",
    "doublelist = [[]]*10\n",
    "doublelist[0].append(1)\n",
    "print(doublelist)\n",
    "# DO\n",
    "doublelist = [[] for _ in range(10)]\n",
    "doublelist[0].append(1)\n",
    "print(doublelist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Numpy\n",
    "Very powerful python tool for handling matrices and higher dimensional arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]]\n",
      "(3, 2)\n",
      "[[1. 1. 1. 1.]\n",
      " [1. 1. 1. 1.]\n",
      " [1. 1. 1. 1.]]\n",
      "(3, 4)\n",
      "[[1. 0. 0. 0. 0.]\n",
      " [0. 1. 0. 0. 0.]\n",
      " [0. 0. 1. 0. 0.]\n",
      " [0. 0. 0. 1. 0.]\n",
      " [0. 0. 0. 0. 1.]]\n",
      "(5, 5)\n",
      "[[-0.16367035 -0.87855847  0.7961741   0.26598743 -1.75846406]\n",
      " [-0.09106335 -0.95040985 -0.84240584  0.5022866   0.40741974]\n",
      " [-0.6448735  -0.94000292 -0.63470733  0.3198772   0.20179754]\n",
      " [ 3.87482256 -2.01679666  1.06469451  0.75220559  0.8659874 ]\n",
      " [ 1.86533616  1.41129369  0.74469198  0.56709733  0.33023962]]\n"
     ]
    }
   ],
   "source": [
    "# create arrays\n",
    "a = np.array([[1,2],[3,4],[5,6]])\n",
    "print(a)\n",
    "print(a.shape)\n",
    "# create all-zero/one arrays\n",
    "b = np.ones((3,4)) # np.zeros((3,4))\n",
    "print(b)\n",
    "print(b.shape)\n",
    "# create identity matrix\n",
    "c = np.eye(5)\n",
    "print(c)\n",
    "print(c.shape)\n",
    "# create random matrix with standard normal init\n",
    "d = np.random.normal(size=(5,5))\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4 5 6 7]\n",
      "[[0 1 2 3 4 5 6 7]]\n"
     ]
    }
   ],
   "source": [
    "# reshaping arrays\n",
    "a = np.arange(8)         # [8,] all vectors are column by default\n",
    "b = a.reshape(1,-1)      # [1,8] row vector -- -1 for auto-fill\n",
    "c = a.reshape((4,2))     # shape [4,2]\n",
    "d = a.reshape((2,2,-1))  # shape [2,2,2] \n",
    "e = c.flatten()          # shape [8,]\n",
    "f = np.expand_dims(a, 0) # [1,8]\n",
    "g = np.expand_dims(a, 1) # [8,1]\n",
    "h = e.squeeze()          # shape[8, ]    -- remove all unnecessary dimensions\n",
    "print(a)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "(3,)\n",
      "(3,)\n",
      "[[1]\n",
      " [2]\n",
      " [3]]\n",
      "(3, 1)\n",
      "(1, 3)\n"
     ]
    }
   ],
   "source": [
    "# be careful about vectors!\n",
    "a = np.array([1,2,3]) # this is a 3-d column vector, which you cannot transpose\n",
    "print(a)\n",
    "print(a.shape)\n",
    "print(a.T.shape)\n",
    "a = a.reshape(-1, 1) # this is a 3x1 matrix, which you can transpose\n",
    "print(a)\n",
    "print(a.shape)\n",
    "print(a.T.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(8, 3)\n",
      "(4, 6)\n"
     ]
    }
   ],
   "source": [
    "# concatenating arrays\n",
    "a = np.ones((4,3))\n",
    "b = np.ones((4,3))\n",
    "c = np.concatenate([a,b], 0)\n",
    "print(c.shape)\n",
    "d = np.concatenate([a,b], 1)\n",
    "print(d.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3. 3. 3. 1. 1. 1. 1. 1. 1. 1.]\n",
      " [3. 3. 3. 1. 1. 1. 1. 1. 1. 1.]\n",
      " [3. 3. 3. 1. 1. 1. 1. 1. 1. 1.]\n",
      " [2. 2. 2. 0. 0. 0. 0. 0. 0. 0.]\n",
      " [2. 2. 2. 0. 0. 0. 0. 0. 0. 4.]\n",
      " [2. 2. 2. 0. 0. 0. 0. 0. 0. 0.]\n",
      " [2. 2. 2. 4. 0. 0. 0. 0. 0. 0.]\n",
      " [2. 2. 2. 0. 0. 4. 0. 0. 0. 0.]\n",
      " [2. 2. 2. 0. 0. 0. 0. 0. 0. 0.]\n",
      " [2. 2. 2. 0. 0. 0. 0. 0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "# access array slices by index\n",
    "a = np.zeros([10, 10])\n",
    "a[:3] = 1\n",
    "a[:, :3] = 2\n",
    "a[:3, :3] = 3\n",
    "rows = [4,6,7]\n",
    "cols = [9,3,5]\n",
    "a[rows, cols] = 4\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3, 4)\n",
      "[[[ 0  1  2  3]\n",
      "  [ 4  5  6  7]\n",
      "  [ 8  9 10 11]]\n",
      "\n",
      " [[12 13 14 15]\n",
      "  [16 17 18 19]\n",
      "  [20 21 22 23]]]\n",
      "(4, 3, 2)\n",
      "[[[ 0 12]\n",
      "  [ 4 16]\n",
      "  [ 8 20]]\n",
      "\n",
      " [[ 1 13]\n",
      "  [ 5 17]\n",
      "  [ 9 21]]\n",
      "\n",
      " [[ 2 14]\n",
      "  [ 6 18]\n",
      "  [10 22]]\n",
      "\n",
      " [[ 3 15]\n",
      "  [ 7 19]\n",
      "  [11 23]]]\n"
     ]
    }
   ],
   "source": [
    "# transposition\n",
    "a = np.arange(24).reshape(2,3,4)\n",
    "print(a.shape)\n",
    "print(a)\n",
    "a = np.transpose(a, (2,1,0)) # swap 0th and 2nd axes\n",
    "print(a.shape)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-2.   1. ]\n",
      " [ 1.5 -0.5]]\n",
      "[[-2.   1. ]\n",
      " [ 1.5 -0.5]]\n",
      "[-1.  1.]\n",
      "[-1.  1.]\n"
     ]
    }
   ],
   "source": [
    "c = np.array([[1,2],[3,4]])\n",
    "print(np.linalg.inv(c))\n",
    "# pinv is pseudo inversion for stability\n",
    "print(np.linalg.pinv(c))\n",
    "# To compute c^-1 b\n",
    "b = np.array([1, 1])\n",
    "print(np.linalg.inv(c)@b)\n",
    "print(np.linalg.solve(c,b)) # preferred!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "11\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "# vector dot product\n",
    "v1 = np.array([1,2])\n",
    "v2 = np.array([3,4])\n",
    "print(v1.dot(v2))\n",
    "print(np.dot(v1,v2))\n",
    "print(v1@v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3 4]\n",
      " [6 8]]\n",
      "[[3 4]\n",
      " [6 8]]\n"
     ]
    }
   ],
   "source": [
    "# vector outer product\n",
    "print(np.outer(v1,v2))\n",
    "print(v1.reshape(-1,1).dot(v2.reshape(1,-1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 5 11]\n",
      "[ 5 11]\n",
      "[ 5 11]\n"
     ]
    }
   ],
   "source": [
    "# Matrix multiply vector (Ax)\n",
    "m = np.array([1,2,3,4]).reshape(2,2)\n",
    "print(m@v1)\n",
    "print(m.dot(v1))\n",
    "print(np.matmul(m, v1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[3. 3.]\n",
      " [3. 3.]\n",
      " [3. 3.]\n",
      " [3. 3.]]\n",
      "[[3. 3.]\n",
      " [3. 3.]\n",
      " [3. 3.]\n",
      " [3. 3.]]\n"
     ]
    }
   ],
   "source": [
    "# matrix multiplication\n",
    "a = np.ones((4,3)) # 4,3\n",
    "b = np.ones((3,2)) # 3,2 --> 4,2\n",
    "print(a @ b)       # same as a.dot(b)\n",
    "print(np.matmul(a,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 4)\n",
      "(4, 1)\n",
      "[[2. 2. 2. 2.]\n",
      " [3. 3. 3. 3.]\n",
      " [4. 4. 4. 4.]\n",
      " [5. 5. 5. 5.]]\n"
     ]
    }
   ],
   "source": [
    "# broadcasting\n",
    "c = np.ones([4,4])\n",
    "# automatic repetition along axis\n",
    "d = np.array([1,2,3,4]).reshape(4,1)\n",
    "print(c.shape)\n",
    "print(d.shape)\n",
    "print(c + d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(15, 1, 5)\n",
      "(1, 15, 5)\n",
      "(15, 15, 5)\n"
     ]
    }
   ],
   "source": [
    "# computing pairwise distance (using broadcasting)\n",
    "samples = np.random.random([15, 5])\n",
    "diff=samples[:,np.newaxis,:]-samples[np.newaxis]\n",
    "print(samples[:,np.newaxis,:].shape)\n",
    "print(samples[np.newaxis,:,:].shape)\n",
    "print(diff.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "numpy spends 0.003999471664428711 seconds\n",
      "list operation spends 8.870983362197876 seconds\n"
     ]
    }
   ],
   "source": [
    "# speed test: numpy vs list\n",
    "a = np.ones((100,100))\n",
    "b = np.ones((100,100))\n",
    "\n",
    "def matrix_multiplication(X, Y):\n",
    "    result = [[0]*len(Y[0]) for _ in range(len(X))]\n",
    "    for i in range(len(X)):\n",
    "        for j in range(len(Y[0])):\n",
    "            for k in range(len(Y)):\n",
    "                result[i][j] += X[i][k] * Y[k][j]\n",
    "    return result\n",
    "\n",
    "import time\n",
    "\n",
    "# run numpy matrix multiplication for 10 times\n",
    "start = time.time()\n",
    "for _ in range(10):\n",
    "    a @ b\n",
    "end = time.time()\n",
    "print(\"numpy spends {} seconds\".format(end-start))\n",
    "\n",
    "# run list matrix multiplication for 10 times\n",
    "start = time.time()\n",
    "for _ in range(10):\n",
    "    matrix_multiplication(a,b)\n",
    "end = time.time()\n",
    "print(\"list operation spends {} seconds\".format(end-start))\n",
    "\n",
    "# the difference gets more significant as matrices grow in size!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2. 2. 2. 2.]\n",
      "4.0\n",
      "16.0\n",
      "[4. 4. 4. 4.]\n",
      "[4. 4. 4. 4.]\n",
      "[[0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]]\n",
      "[[2.71828183 2.71828183 2.71828183 2.71828183]\n",
      " [2.71828183 2.71828183 2.71828183 2.71828183]\n",
      " [2.71828183 2.71828183 2.71828183 2.71828183]\n",
      " [2.71828183 2.71828183 2.71828183 2.71828183]]\n",
      "[[0.84147098 0.84147098 0.84147098 0.84147098]\n",
      " [0.84147098 0.84147098 0.84147098 0.84147098]\n",
      " [0.84147098 0.84147098 0.84147098 0.84147098]\n",
      " [0.84147098 0.84147098 0.84147098 0.84147098]]\n",
      "[[3. 3. 3. 3.]\n",
      " [3. 3. 3. 3.]\n",
      " [3. 3. 3. 3.]\n",
      " [3. 3. 3. 3.]]\n"
     ]
    }
   ],
   "source": [
    "# other common operations\n",
    "a = np.ones((4,4))\n",
    "print(np.linalg.norm(a, axis=0))\n",
    "print(np.linalg.norm(a))\n",
    "print(np.sum(a)) # sum all elements in matrix\n",
    "print(np.sum(a, axis=0)) # sum along axis 0\n",
    "print(np.sum(a, axis=1)) # sum along axis 1\n",
    "# element-wise operations, for examples\n",
    "print(np.log(a))\n",
    "print(np.exp(a))\n",
    "print(np.sin(a))\n",
    "# operation with scalar is interpreted as element-wise\n",
    "print(a * 3) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nan\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-2-84f2c78182a7>:4: RuntimeWarning: invalid value encountered in true_divide\n",
      "  print(a/b)\n"
     ]
    }
   ],
   "source": [
    "# invalid operations result in an NaN\n",
    "a = np.array(0)\n",
    "b = np.array(0)\n",
    "print(a/b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Matplotlib\n",
    "Powerful tool for visualization <br/>\n",
    "Many tutorials online. We only go over the basics here <br/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1c1bb9fbee0>]"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# line plot\n",
    "x = np.arange(0, 2, 0.01)\n",
    "y = 1+np.sin(2*np.pi*x)\n",
    "plt.plot(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x1c1ba390670>"
      ]
     },
     "execution_count": 216,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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0SE17K//F8682F/BZs2apTlz5ujdd9/Viy++qIMHD4bURHKPPddhn5CQIJ/PF7QWCATU1NQU8lcjfGnixIlB/x0dHa1p06bp7t27w9TR0CsrK1N+fr5SUlJ08ODBkJl8hf31pXDnJbG/fD6fysvLZT3xO6OcTqeSkpJUX18fUh/JPfZch31GRob8fr9u3rzZvfbVQ42vP1SCtG/fPmVnZwfdSTx48EC3bt3SrFmzhrGzoVNeXq6NGzdq8eLFKi0tVUxMTK+17C9782J/ffncYv369bp48WL32hdffKHPPvtMiYmJIfWR3GPPVdg/fvxYfr9fHR0dkiS32620tDQVFhbqypUrOn/+vIqLi7VkyRJNmTJlmLsdfl+fl8fjUVtbmzZt2qQbN27oypUrWr16tSZMmKClS5cOc7eDz+v1qqioSFlZWdqwYYOam5vl9/vl9/vV3NzM/voau/MyfX9J0pw5c5SVlaXi4mJVVVWppqZGmzZtUnNzs1asWDG4e6yfHxd9JmzatCnoc+Off/65lZycbB09erR77d69e9aaNWusl19+2crMzLSKioqs9vb24Wh32IUzr08++cTKy8uz0tPTrbS0NGvNmjXW559/PhztDrkDBw5YycnJPX7l5uayv76mP/MyeX99pbm52Xr77betb3/729a3vvUt61e/+pV19epVy7IGN8P4heMAYIDn6hgHANAzwh4ADEDYA4ABCHsAMABhDwAGIOwBwACEPQAYgLAHAAMQ9gBggP8D2F4jpm4KgNEAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# scatter plot\n",
    "x = [1,3,2]\n",
    "y = [1,2,3]\n",
    "plt.scatter(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 3 artists>"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAD/CAYAAAD8MdEiAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAbHklEQVR4nO3df0yU9x0H8Ped9YZ4RvR2Qi1mGvmV0noCAtaB1DOzM13jomvEzmKRrXMTjRUqrSmoGRansSQMNMSJTOvqEp0bRE3czJoso4BolFUt548h3Ti4wx3ym1P47g8j8Tz07vHuhOP7fiX8cV8+D/f9+NF7w/NwjyohhAAREUlLPdIbICKikcUgICKSHIOAiEhyDAIiIskxCIiIJMcgICKSHIOAiEhyL4z0Bp7GZuvG4OCDtznodFrcudM1wjvyjbHaG/vyP2O1N1n6UqtVmDJlouKvM6qDYHBQDAXBw8dj1VjtjX35n7HaG/t6Mp4aIiKSHIOAiEhybgVBa2srNm/ejMTERMTExOD999/H9evXn1hvs9mQlZWFhIQExMfHIzc3F93d3V7bNBEReY/LIBBC4Oc//zlaWlpw8OBBHD9+HAEBAXjvvfee+OK+ceNGNDU14dChQyguLkZVVRXy8vK8vnkiIvKcyyBoa2vD7NmzsXPnTrzyyiuYPXs2fvWrX6GtrQ0mk8mp/uLFi6itrUVBQQGio6ORmJiI/Px8nDp1Cs3NzT5pgoiInp3LINDr9SgsLMSsWbMAPAiGgwcPYtq0aYiIiHCqr6urg06nQ1hY2NBaXFwcVCoV6urqvLh1IiLyBkW/PvrRRx/h5MmT0Gg02L9/PyZOdP59VYvFgpCQEIc1jUaDKVOmoKWlxbPdEhGR1ykKgoyMDPz0pz/FH/7wB6xfvx5Hjx7FK6+84lDT29sLjUbjdKxGo0F/f7+izel0WofHev0kRcf7k7Ham7t92e8NQDN+nI934z3+NC+lf7b+1JsS7OvJFAVBeHg4AGDnzp24fPkyjhw5gt/85jcONQEBAbDb7U7H2u12BAYGKtrcnTtdQ2+W0OsnwWrtVHS8vxirvSnpS6+fhLey/uLjHcmpcu8yRXOQ/e+iP3m8L7Va5fQNtDtcXiOwWCyorKzEo/+jpVqtRlhYGFpbW53qQ0JCYLFYHNbsdjtsNpvTKSMiIhp5LoPAbDYjOzsbFy5cGFq7d+8erl69itmzZzvVx8fHw2q14tatW0NrDy8Sz5s3zxt7JiIiL3IZBK+++ioSExORl5eHuro6mEwm5OTkoL29He+99x4GBgZgtVrR19cHADAYDIiNjUVWVhbq6+tRW1uLvLw8LFu2DMHBwT5viIiIlHEZBGq1Gr/97W8RFxeHTZs24e2338bdu3dx9OhRzJgxA2azGUlJSTh9+jQAQKVSobi4GDNmzMCaNWuwYcMGLFiwANu3b/d1L0RE9Azculg8efJk/PrXvx72c6GhoWhoaHBY0+l0KCoq8nx3RETkc7zpHBGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUnOrSDo6urCp59+CqPRiJiYGCxfvhznzp17Yv2xY8cQGRnp9HH79m2vbZyIiLzjBXeKPv74YzQ0NCA/Px8vvfQSzpw5g8zMTJSVleG1115zqm9oaEBycjIKCgoc1qdOneqdXRMRkde4DAKr1YqzZ8+itLQUCxYsAACsW7cOX331FY4fPz5sEJhMJsTExECv13t/x0RE5FUuTw1NmDABBw4cwLx58xzWVSoV7t69O+wxJpMJYWFh3tkhERH5lMsg0Gq1WLhwIbRa7dDapUuXUF1djddff92p3mw2o6OjA1VVVXjzzTeRnJyMzMxMNDY2enPfRETkJW5dI3jUzZs3kZmZCYPBgJUrVzp93mQyAQDUajV2796Nnp4e7Nu3D6mpqaisrFR0ukin0zo81usnKd2u3xirvY3VvvyNkjmM1ZmxrydTFATnz59HZmYmpk+fjtLSUowfP96pJiUlBTU1NQgKChpaKykpwaJFi3DixAmsW7fO7ee7c6cLg4MCwINmrdZOJdv1G2O1NyV9jdV/pKOFkjnI/nfRnzzel1qtcvoG2h1uv4+goqIC6enpiI6OxpEjRxxe6B/3+OcCAwMRGhqK5uZmxRskIiLfcisIKisrsWXLFixduhSlpaUO1wseV1ZWhqSkJNjt9qG1zs5ONDY2Ijw83PMdExGRV7kMgpaWFuTm5iIxMREffvgh2tvbYbVaYbVa0d7ejoGBAVitVvT19QEAjEYjenp6kJOTgxs3bqC+vh7r16/H5MmTsWLFCp83REREyrgMgrNnz6K3txfV1dVITk5GUlLS0Mcvf/lLmM1mJCUl4fTp0wCAmTNnory8HDabDampqUhPT0dQUBAOHz6MwMBAnzdERETKuLxYnJaWhrS0tKfWNDQ0ODyeM2cOysvLPdoYERE9H7zpHBGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESSYxAQEUmOQUBEJDkGARGR5BgERESScysIurq68Omnn8JoNCImJgbLly/HuXPnnlhvs9mQlZWFhIQExMfHIzc3F93d3V7bNBEReY9bQfDxxx/jyy+/RH5+Pv785z9jyZIlyMzMxFdffTVs/caNG9HU1IRDhw6huLgYVVVVyMvL8+rGiYjIO1wGgdVqxdmzZ7F161YsWLAA3/ve97Bu3TokJCTg+PHjTvUXL15EbW0tCgoKEB0djcTEROTn5+PUqVNobm72SRNERPTsXAbBhAkTcODAAcybN89hXaVS4e7du071dXV10Ol0CAsLG1qLi4uDSqVCXV2dF7ZMRETe5DIItFotFi5cCK1WO7R26dIlVFdX4/XXX3eqt1gsCAkJcVjTaDSYMmUKWlpaPN8xERF51QtKD7h58yYyMzNhMBiwcuVKp8/39vZCo9E4rWs0GvT39yt6Lp1O6/BYr5+kbLN+ZKz2Nlb78jdK5uBurf3eADTjxz3rlp47f/q7qOTP1ht9KQqC8+fPIzMzE9OnT0dpaSnGjx/vVBMQEAC73e60brfbERgYqGhzd+50YXBQAHjQrNXaqeh4fzFWe1PSlz/9I/VHSuagpPatrL94si16gsq9y9yaw+PzUqtVTt9Au8Pt9xFUVFQgPT0d0dHROHLkCIKCgoatCwkJgcVicViz2+2w2WxOp4yIiGjkuRUElZWV2LJlC5YuXYrS0lKH6wWPi4+Ph9Vqxa1bt4bWHl4kfvyCMxERjTyXQdDS0oLc3FwkJibiww8/RHt7O6xWK6xWK9rb2zEwMACr1Yq+vj4AgMFgQGxsLLKyslBfX4/a2lrk5eVh2bJlCA4O9nlDRESkjMtrBGfPnkVvby+qq6uRnJzs8LnY2Fjs2bMHixcvRkFBAZYvXw6VSoXi4mLs2LEDa9asgUajwRtvvIGtW7f6rAkiInp2LoMgLS0NaWlpT61paGhweKzT6VBUVOTZzoiI6LngTeeIiCTHICAikhyDgIhIcgwCIiLJMQiIiCTHICAikhyDgIhIcgwCIiLJMQiIiCTHICAikhyDgIhIcgwCIiLJMQiIiCTHICAikhyDgIhIcgwCIiLJMQiIiCTHICAikhyDgIhIcgwCIiLJMQiIiCTHICAikhyDgIhIcoqDoLS0FKtWrXpqzbFjxxAZGen0cfv27WfeKBER+cYLSoqPHj2KwsJCxMTEPLWuoaEBycnJKCgocFifOnWq8h0SEZFPuRUEra2t2LZtG2pqajBr1iyX9SaTCTExMdDr9R5vkIiIfMutU0NXrlzBxIkTUVFRAYPB4LLeZDIhLCzM480REZHvufUTgdFohNFodOsLms1mdHR0oKqqCgcOHEBHRwcMBgOys7Mxc+ZMT/ZKREQ+oOgagTtMJhMAQK1WY/fu3ejp6cG+ffuQmpqKyspKRaeLdDqtw2O9fpJX9zqajNXexmpf/kbJHDiz0cHdOXhjXl4PgpSUFNTU1CAoKGhoraSkBIsWLcKJEyewbt06t7/WnTtdGBwUAB40a7V2enu7o8JY7U1JX3zx8S0lc+DMRgd35vD4vNRqldM30O7wyfsIHg0BAAgMDERoaCiam5t98XREROQBrwdBWVkZkpKSYLfbh9Y6OzvR2NiI8PBwbz8dERF5yOMgGBgYgNVqRV9fH4AHF5Z7enqQk5ODGzduoL6+HuvXr8fkyZOxYsUKjzdMRETe5XEQmM1mJCUl4fTp0wCAmTNnory8HDabDampqUhPT0dQUBAOHz6MwMBAjzdMRETepfhi8a5duxweh4aGoqGhwWFtzpw5KC8v92hjRET0fPCmc0REkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJTnEQlJaWYtWqVU+tsdlsyMrKQkJCAuLj45Gbm4vu7u5n3iQREfmOoiA4evQoCgsLXdZt3LgRTU1NOHToEIqLi1FVVYW8vLxn3iQREfnOC+4Utba2Ytu2baipqcGsWbOeWnvx4kXU1tbi1KlTCAsLAwDk5+cjPT0dWVlZmD59uue7JiIir3HrJ4IrV65g4sSJqKiogMFgeGptXV0ddDrdUAgAQFxcHFQqFerq6jzbLREReZ1bPxEYjUYYjUa3vqDFYkFISIjDmkajwZQpU9DS0qJ8h0RE5FNuBYESvb290Gg0TusajQb9/f2KvpZOp3V4rNdPcus4+70BaMaPU/RcI83d3kaa0j9bf+lrrFMyB85sdHB3Dt6Yl9eDICAgAHa73WndbrcjMDBQ0de6c6cLg4MCwINmrdZOt47T6yfhray/KHouck/l3mWK5qCklnyHM/M/7szh8Xmp1Sqnb6Dd4fX3EYSEhMBisTis2e122Gw2p1NGREQ08rweBPHx8bBarbh169bQ2sOLxPPmzfP20xERkYc8DoKBgQFYrVb09fUBAAwGA2JjY5GVlYX6+nrU1tYiLy8Py5YtQ3BwsMcbJiIi7/I4CMxmM5KSknD69GkAgEqlQnFxMWbMmIE1a9Zgw4YNWLBgAbZv3+7pUxERkQ8ovli8a9cuh8ehoaFoaGhwWNPpdCgqKvJsZ0RE9FzwpnNERJJjEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkObeCYHBwEEVFRUhOTobBYMDatWtx+/btJ9YfO3YMkZGRTh9PO4aIiEbGC+4UlZSU4IsvvsCuXbsQHByMvXv3IiMjA6dOncJ3vvMdp/qGhgYkJyejoKDAYX3q1Kne2TUREXmNy58I7HY7ysrKkJmZiZSUFERFRaGwsBBtbW04c+bMsMeYTCZERUVBr9c7fIwbN87rDRARkWdcBsG1a9fQ09OD+fPnD61ptVq8/PLLqKurG/YYk8mEsLAw7+2SiIh8xmUQtLa2AgCCg4Md1qdNmwaz2exUbzab0dHRgaqqKrz55ptITk5GZmYmGhsbvbNjIiLyKpfXCHp7ewEAGo3GYV2j0cButzvVm0wmAIBarcbu3bvR09ODffv2ITU1FZWVldDr9W5vTqfTOjzW6ye5fSz5jpI5cGajA2fmf9ydgzfm5TIIAgICADy4VvBoGNjtdgQGBjrVp6SkoKamBkFBQUNrJSUlWLRoEU6cOIF169a5vbk7d7owOCgAPGjWau106zj+RfYtJXPgzEYHzsz/uDOHx+elVqucvoF2h8tTQy+++CIAwGKxOKxbLBan00UPPRoCABAYGIjQ0FA0Nzcr3iAREfmWyyCIioqCVqtFbW3t0FpXVxeuXr2KhIQEp/qysjIkJSU5nDbq7OxEY2MjwsPDvbRtIiLyFpdBoNFosHr1ahQWFuJvf/sbvvnmG3zwwQcIDg7GkiVLMDAwAKvVir6+PgCA0WhET08PcnJycOPGDdTX12P9+vWYPHkyVqxY4fOGiIhIGbfeWbxx40a8/fbbyMvLw6pVqyCEwO9+9ztoNBqYzWYkJSXh9OnTAICZM2eivLwcNpsNqampSE9PR1BQEA4fPjzsNQUiIhpZbr2zeNy4ccjOzkZ2drbT50JDQ9HQ0OCwNmfOHJSXl3tlg0RE5Fu86RwRkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREkmMQEBFJjkFARCQ5BgERkeQYBEREknMrCAYHB1FUVITk5GQYDAasXbsWt2/ffmK9zWZDVlYWEhISEB8fj9zcXHR3d3tt00RE5D1uBUFJSQm++OIL5Ofn449//CPGjRuHjIwM9Pf3D1u/ceNGNDU14dChQyguLkZVVRXy8vK8unEiIvIOl0Fgt9tRVlaGzMxMpKSkICoqCoWFhWhra8OZM2ec6i9evIja2loUFBQgOjoaiYmJyM/Px6lTp9Dc3OyTJoiI6Nm5DIJr166hp6cH8+fPH1rTarV4+eWXUVdX51RfV1cHnU6HsLCwobW4uDioVKph64mIaGS94KqgtbUVABAcHOywPm3aNJjNZqd6i8WCkJAQhzWNRoMpU6agpaVF0ebUatVTHz/NtCkTFD0XuU/JHDiz0YEz8z/uzuHROiWze5TLIOjt7QXw4MX8URqNBna7fdj6x2sf1j/pmsKTTJky0eGxTqd1+9iDnyxR9FzkPiVz4MxGB87M/7g7ByXzehKXp4YCAgIAwOlF3263IzAwcNj64QLiSfVERDSyXAbBiy++CODBKZ9HWSwWp9NFABASEuJUa7fbYbPZnE4ZERHRyHMZBFFRUdBqtaitrR1a6+rqwtWrV5GQkOBUHx8fD6vVilu3bg2tPbxIPG/ePG/smYiIvMjlNQKNRoPVq1ejsLAQ3/3udxEaGoq9e/ciODgYS5YswcDAAP73v/9h0qRJCAgIgMFgQGxsLLKysrBjxw709fUhLy8Py5YtG/YnCCIiGlkqIYRwVTQwMIDCwkL86U9/Qm9vL+Li4rBt2zbMmDED//nPf7B48WIUFBRg+fLlAIA7d+5gx44d+Mc//gGNRoM33ngDW7duHbreQEREo4dbQUBERGMXbzpHRCQ5BgERkeQYBEREkhsVQaD0NtfHjh1DZGSk08fTjhkNSktLsWrVqqfW+OMtvN3py19m1tXVhU8//RRGoxExMTFYvnw5zp0798R6f5qX0t78ZWatra3YvHkzEhMTERMTg/fffx/Xr19/Yr2/zExpXx7NS4wCRUVFYv78+eLLL78U165dEz/72c/E4sWLRV9f37D127dvFxkZGcJisTh83L9//znv3H2ff/65iIyMFKmpqU+tW716tfjJT34ivv76a1FdXS2MRqPYvHnzc9qlcu725S8zy8zMFD/4wQ/EP//5T9HY2Cj2798voqKiRFVV1bD1/jQvpb35w8wGBwfFW2+9JVatWiX+9a9/iRs3bogNGzaIBQsWiK6urmGP8YeZPUtfnsxrxIOgv79fzJ07V3z++edDa52dncJgMIiTJ08Oe8w777wj9uzZ87y26JGWlhbxi1/8QsydO1f88Ic/fOoL5oULF0RERIS4fv360FpVVZWIjIwU//3vf5/Hdt2mpC8h/GNmFotFREREiL///e8O62lpacO+UPjTvJT2JoT/zGzTpk3i1q1bQ2vXrl0TERER4uLFi071/jIzpX0J4dm8RvzUkNLbXAOAyWRyuM31aHblyhVMnDgRFRUVMBgMT631p1t4K+kL8I+ZTZgwAQcOHHB6B7xKpcLdu3ed6v1pXkp7A/xjZnq9HoWFhZg1axYAoK2tDQcPHsS0adMQERHhVO8vM1PaF+DZvFy+s9jXlN7m2mw2o6OjA1VVVThw4AA6OjpgMBiQnZ2NmTNnPo8tK2I0GmE0Gt2q9eYtvH1NSV/+MjOtVouFCxc6rF26dAnV1dX45JNPnOr9aV5Ke/OXmT3qo48+wsmTJ6HRaLB//35MnDjRqcafZvaQO315Oq8R/4lA6W2uTSYTAECtVmP37t347LPP0N3djdTUVFitVt9v2Ie8eQvv0cRfZ3bz5k1kZmbCYDBg5cqVTp/353m56s0fZ5aRkYHjx4/jRz/6EdavX4+vv/7aqcYfZ+ZOX57Oa8SDQOltrlNSUlBTU4Ndu3YhOjoa8fHxKCkpgRACJ06ceC579pWxegtvf5zZ+fPn8c4770Cv16O0tBTjx493qvHXebnTmz/OLDw8HK+++ip27tyJl156CUeOHHGq8ceZudOXp/Ma8SBQeptrAAgKCnJ4HBgYiNDQUL//P5HH8i28/WlmFRUVSE9PR3R0NI4cOeK094f8cV7u9gb4x8wsFgsqKyshHrlTjlqtRlhY2NBp50f5y8yU9gV4Nq8RDwKlt7kuKytDUlKSQ6p3dnaisbER4eHhz2XPvjJWb+HtTzOrrKzEli1bsHTpUpSWlkKrffL//uRv81LSm7/MzGw2Izs7GxcuXBhau3fvHq5evYrZs2c71fvLzJT25fG8nul3jbzss88+EwkJCeKvf/3r0PsIlixZIvr7+8X9+/eFxWIRvb29Qggh/v3vf4uYmBixadMmcf36dXH58mXx7rvvikWLFonu7u4R7uTpcnJyHH7N8vHeBgcHRWpqqvjxj38sLl++LGpqasTixYtFTk7OSG3ZLa768peZmc1mYTAYRFpammhtbXX4XWybzebX81Lam7/MbGBgQLz77rti6dKl4vz586KhoUF88MEHIi4uTjQ1NfntzJT25em8RkUQ3L9/X+zZs0e89tprYu7cuSIjI0M0NTUJIYT49ttvRUREhDhx4sRQ/eXLl8WaNWtEXFyciI2NFRs2bBDffvvtSG3fbY+/YA7XW1tbm9iwYYOYO3euSEhIELm5uUPDHq3c6csfZvb73/9eREREDPuRmprq1/N6lt78YWZCCNHe3i4++eQT8f3vf1/MmTNHrF27VnzzzTdCCP/+N6a0L0/mxdtQExFJbsSvERAR0chiEBARSY5BQEQkOQYBEZHkGARERJJjEBARSY5BQEQkOQYBEZHkGARERJL7P/uDK6txmbmAAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# bar plots\n",
    "plt.bar(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x1c1ba021fa0>"
      ]
     },
     "execution_count": 218,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot configurations\n",
    "x = [1,2,3]\n",
    "y1 = [1,3,2]\n",
    "y2 = [4,0,4]\n",
    "\n",
    "# set figure size\n",
    "plt.figure(figsize=(5,5))\n",
    "\n",
    "# set axes\n",
    "plt.xlim(0,5)\n",
    "plt.ylim(0,5)\n",
    "plt.xlabel(\"x label\")\n",
    "plt.ylabel(\"y label\")\n",
    "\n",
    "# add title\n",
    "plt.title(\"My Plot\")\n",
    "\n",
    "plt.plot(x,y1, label=\"data1\", color=\"red\", marker=\"*\", dashes=[5,1])\n",
    "plt.plot(x,y2, label=\"data2\", color=\"green\", marker=\".\")\n",
    "plt.grid()\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 4 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# subplots\n",
    "f, ax = plt.subplots(2,2,figsize=(5,5))\n",
    "ax[0][0].plot(x,y)\n",
    "ax[0][1].scatter(x,y)\n",
    "ax[1][0].bar(x,y)\n",
    "ax[1][1].hist(x,y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PolyCollection at 0x1c1ba20d400>"
      ]
     },
     "execution_count": 220,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# plot area under curve\n",
    "probs = [1, 1, 0.95, 0.9, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]\n",
    "thres = np.arange(0,1,0.1)\n",
    "plt.fill_between(x=thres, y1=probs, y2=0, step='post')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sn\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "array = [[13,1,1,0,2,0],\n",
    "         [3,9,6,0,1,0],\n",
    "         [0,0,16,2,0,0],\n",
    "         [0,0,0,13,0,0],\n",
    "         [0,0,0,0,15,0],\n",
    "         [0,0,1,0,0,15]]\n",
    "labels = 'A B C D E F'.split(' ')\n",
    "sn.heatmap(array, annot=True, annot_kws={\"size\": 16}, cmap=\"rocket_r\")\n",
    "plt.xticks(ticks=np.arange(len(labels))+0.5,labels=labels)\n",
    "plt.yticks(ticks=np.arange(len(labels))+0.5,labels=labels,rotation=0)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}