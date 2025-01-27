%global _name dateutil
%global _description The dateutil module provides powerful extensions to the standard datetime module, available in Python.

Name:       python-dateutil
Version:    2.8.1
Release:    5
Summary:    Powerful extensions to datetime
License:    Apache 2.0 or BSD
URL:        https://github.com/dateutil/dateutil
Source0:    https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-%{version}.tar.gz	

BuildArch:  noarch
Buildrequires:  gdb

%description
%{_description}

%package -n python3-%{_name}
Summary:    %{summary}
Buildrequires:  python3-devel python3-setuptools python3-setuptools_scm python3-six python3-pytest python3-freezegun python3-hypothesis
Requires:       python3-six tzdata
%{?python_provide:%python_provide python3-%{_name}}

%description -n python3-%{_name}
%{_description}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
rm setup.cfg
export LANG=en_US.UTF-8
%{__python3} -m pytest

%files -n python3-%{_name}
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{_name}/
%{python3_sitelib}/*info

%files help
%defattr(-,root,root)
%doc NEWS PKG-INFO RELEASING

%changelog
* Wed Jan 26 2022 zhangy1317<zhangy1317@chinaunicom.cn> - 1:2.8.1-5
- Remove python2

* Tue May 25 2021 chengshaowei<chenshaowei3@huawei.com> - 1:2.8.1-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix failure in check

* Mon May 24 2021 chengshaowei<chenshaowei3@huawei.com> - 1:2.8.1-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: fix failure in make check

* Wed May 13 2020 wangchen<wangchen137@huawei.com> - 1:2.8.1-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:delete python-dateutil-2.7.0.tar.gz

* Mon May 11 2020 openEuler Buildteam<buildteam@openeuler.org> - 1:2.8.1-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update to 2.8.1

* Fri Sep 27 2019 shenyangyang<shenyangyang4@huawei.com> - 1:2.7.0-7
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify the license

* Fri Sep 27 2019 shenyangyang<shenyangyang4@huawei.com> - 1:2.7.0-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:move license file

* Thu Sep 5 2019 shenyangyang<shenyangyang4@huawei.com> - 1:2.7.0-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:optimize the method to provide default version of python-name

* Fri Aug 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:2.7.0-4
- Package init
