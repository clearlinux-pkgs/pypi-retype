#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-retype
Version  : 21.12.0
Release  : 42
URL      : https://files.pythonhosted.org/packages/01/c5/f4c3e9bc4fc21be32bc83b2db99eb439fc60e657ee130ca807358cb2dd26/retype-21.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/c5/f4c3e9bc4fc21be32bc83b2db99eb439fc60e657ee130ca807358cb2dd26/retype-21.12.0.tar.gz
Summary  : re-apply types from .pyi stub files to your codebase
Group    : Development/Tools
License  : MIT
Requires: pypi-retype-bin = %{version}-%{release}
Requires: pypi-retype-license = %{version}-%{release}
Requires: pypi-retype-python = %{version}-%{release}
Requires: pypi-retype-python3 = %{version}-%{release}
Requires: pathspec
Requires: typed_ast
BuildRequires : buildreq-distutils3
Provides: retype
Provides: retype-python
Provides: retype-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(click)
BuildRequires : pypi(pathspec)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(typed_ast)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : typed_ast
BuildRequires : virtualenv

%description
# retype
[![Latest version on
PyPi](https://badge.fury.io/py/retype.svg)](https://badge.fury.io/py/retype)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/retype.svg)](https://pypi.org/project/retype/)
![check](https://github.com/ambv/retype/workflows/check/badge.svg)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/retype/month)](https://pepy.tech/project/retype/month)

%package bin
Summary: bin components for the pypi-retype package.
Group: Binaries
Requires: pypi-retype-license = %{version}-%{release}

%description bin
bin components for the pypi-retype package.


%package license
Summary: license components for the pypi-retype package.
Group: Default

%description license
license components for the pypi-retype package.


%package python
Summary: python components for the pypi-retype package.
Group: Default
Requires: pypi-retype-python3 = %{version}-%{release}

%description python
python components for the pypi-retype package.


%package python3
Summary: python3 components for the pypi-retype package.
Group: Default
Requires: python3-core
Provides: pypi(retype)
Requires: pypi(click)
Requires: pypi(pathspec)
Requires: pypi(typed_ast)

%description python3
python3 components for the pypi-retype package.


%prep
%setup -q -n retype-21.12.0
cd %{_builddir}/retype-21.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641490431
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-retype
cp %{_builddir}/retype-21.12.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-retype/f037b5ef1125b5a7f79d85910c7ae8ee6955df7b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/retype

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-retype/f037b5ef1125b5a7f79d85910c7ae8ee6955df7b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
