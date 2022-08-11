.PHONY : clean
clean :
	@rm -rf ../../temp

# python
PYTHON3 = /usr/bin/python3

.PHONY : preprocess
preprocess : clean
	@mkdir ../../temp
	@touch ../../temp/result.txt
	@$(PYTHON3) ./generate.py

define python3f
	@echo 'python3 $(1)' >> ../../temp/result.txt
	$(PYTHON3) pyproc$(1).py >> ../../temp/result.txt
endef

.PHONY : python3
python3: preprocess
	$(call python3f,0)
	$(call python3f,1)
	$(call python3f,2)

# pypy
# https://www.pypy.org/posts/2022/07/m1-support-for-pypy.html
# https://buildbot.pypy.org/nightly/py3.8/
PYPY3 = /Users/piperliu/Github/downloads/pypy-c-jit-105934-1b027cda9f26-macos_arm64/bin/pypy3.8

define pypy3f
	@echo 'pypy3 $(1)' >> ../../temp/result.txt
	$(PYPY3) pyproc$(1).py >> ../../temp/result.txt
endef

.PHONY : pypy3
pypy3: preprocess
	$(call pypy3f,0)
	$(call pypy3f,1)
	$(call pypy3f,2)

# cpp
CC=/usr/bin/g++
CPPFLAGS=-Idist-jsoncpp -std=c++17
CPP_SRC=dist-jsoncpp/jsoncpp.cpp

define cppf
	@echo 'cpp $(1)' >> ../../temp/result.txt
	$(CC) $(CPPFLAGS) $(CPP_SRC) ./cppproc$(1).cpp -o ../../temp/a$(1).out
	../../temp/a$(1).out >> ../../temp/result.txt
endef

.PHONY : cpp
cpp: preprocess
	$(call cppf,0)
	$(call cppf,1)
	$(call cppf,2)

# go
GO=/usr/local/go/bin/go

define gof
	@echo 'go $(1)' >> ../../temp/result.txt
	$(GO) run goproc$(1).go >> ../../temp/result.txt
endef

.PHONY : go
go: preprocess
	$(call gof,0)
	$(call gof,1)
	$(call gof,2)

# js
JS=/usr/local/bin/node

define jsf
	@echo 'js $(1)' >> ../../temp/result.txt
	$(JS) jsproc$(1).js >> ../../temp/result.txt
endef

.PHONY : js
js: preprocess
	$(call jsf,0)
	$(call jsf,1)
	$(call jsf,2)

.PHONY : all
all: python3 pypy3 cpp go js
