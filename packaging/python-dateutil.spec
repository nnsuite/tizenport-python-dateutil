Name:           python-dateutil
Version:        2.6.1
Release:        0
Url:            https://github.com/dateutil/dateutil
Summary:        Python datetime module
License:        Simplified BSD
Group:          Development/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
The dateutil module provides powerful extensions to the standard datetime module, available in Python.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot} --prefix %{_prefix}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
* Fri Oct 24 2017 Jiho Chu <jiho.chu@samsung.com> - 2.6.1
- Initial import

