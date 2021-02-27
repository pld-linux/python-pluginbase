#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 module for development of flexible plugin systems in Python
Summary(pl.UTF-8):	Moduł Pythona 2 do tworzenia elastycznych systemów wtyczek w Pythonie
Name:		python-pluginbase
Version:	1.0.0
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pluginbase/
Source0:	https://files.pythonhosted.org/packages/source/p/pluginbase/pluginbase-%{version}.tar.gz
# Source0-md5:	f85d8c9cb4d30e90da157a22d11dc727
URL:		https://pypi.org/project/pluginbase/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PluginBase is a module for Python that enables the development of
flexible plugin systems in Python.

%description -l pl.UTF-8
PluginBase to moduł Pythona pozwalający na tworzenie elastycznych
systemów wtyczek w Pythonie.

%package -n python3-pluginbase
Summary:	Python 3 module for development of flexible plugin systems in Python
Summary(pl.UTF-8):	Moduł Pythona 3 do tworzenia elastycznych systemów wtyczek w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pluginbase
PluginBase is a module for Python that enables the development of
flexible plugin systems in Python.

%description -n python3-pluginbase -l pl.UTF-8
PluginBase to moduł Pythona pozwalający na tworzenie elastycznych
systemów wtyczek w Pythonie.

%package apidocs
Summary:	API documentation for Python pluginbase module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pluginbase
Group:		Documentation

%description apidocs
API documentation for Python pluginbase module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pluginbase.

%prep
%setup -q -n pluginbase-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
cd tests
PYTHONPATH=.. \
%{__python} -m pytest
cd ..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd tests
PYTHONPATH=.. \
%{__python3} -m pytest
cd ..
%endif
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/pluginbase.py[co]
%{py_sitescriptdir}/pluginbase-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pluginbase
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pluginbase.py
%{py3_sitescriptdir}/__pycache__/pluginbase.cpython-*.py[co]
%{py3_sitescriptdir}/pluginbase-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
