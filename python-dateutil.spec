%global _name dateutil
%global _description The dateutil module provides powerful extensions to the standard datetime module, available in Python.

Name:       python-dateutil
Version:    2.8.2
Release:    2
Epoch:      1
Summary:    Powerful extensions to datetime
License:    Apache 2.0 or BSD or Python
URL:        https://github.com/dateutil/dateutil
Source0:    https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-%{version}.tar.gz	

BuildArch:  noarch
Buildrequires:  gdb

%description
%{_description}

%package -n python3-%{_name}
Summary:    %{summary}
Buildrequires:  python3-devel python3-setuptools python3-setuptools_scm python3-six
Buildrequires:  python3-pytest python3-freezegun python3-hypothesis python3-sortedcontainers
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
* Wed Jan 05 2022 shixuantong <shixuantong@huawei.com> - 2.8.2-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add python3-sortedcontainers to Buildrequires

* Sat Nov 13 2021 liudabo<liudabo1@huawei.com> - 2.8.2-1
- Type:NA
- ID:NA
- SUG:NA
- DESC:update version to 2.8.2

* Tue Jan 19 2021 tianwei<tianwei12@huawei.com> - 2.8.1-3
- Type:NA
- ID:NA
- SUG:NA
- DESC: fix Unknown pytest.mark.no_cover fail in make check

* Fri Oct 30 2020 shixuantong<shixuantong@huawei.com> - 2.8.1-2
- Type:NA
- ID:NA
- SUG:NA
- DESC:remove python2 dependency

* Thu Jul 23 2020 dingyue<dingyue5@huawei.com> - 1:2.8.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify the license

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
