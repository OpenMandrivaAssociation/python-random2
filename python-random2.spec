%define fname	random2

Name:		python-random2
Summary:	Python 2’s random module for Python 3
Version:	1.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/ee/b5/5aca5217501fbd06b1e5aed6d5986baa0da5380880e6bb6f421ed18e3a32/%{fname}-%{version}.zip
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
%doc README.txt
%{python3_sitelib}/%{fname}*
%{python3_sitelib}/__pycache__/*
