%define fname	random2

Name:		python-random2
Summary:	Python 2’s random module for Python 3
Version:	1.0.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/%{fname}/random2-%{version}.tar.gz
URL:		https://pypi.python.org/pypi/random2
Group:		Development/Python
License:	BSD
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
This package provides a Python 3 ported version of Python 2.7’s
random module. It has also been back-ported to work in Python 2.6.

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot} --skip-build

%files
%{python3_sitelib}/%{fname}*
