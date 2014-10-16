# TODO: qtdemo? (LGPL v2.1+exception/GPL v3 licensed)
#
# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtdoc
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 qtdoc documentation module
Summary(pl.UTF-8):	Moduł dokumentacji Qt5 qtdoc
Name:		qt5-%{orgname}
Version:	5.3.2
Release:	1
License:	FDL v1.3
Group:		Documentation
Source0:	http://download.qt-project.org/official_releases/qt/5.3/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	9126d5842d549089935c3c8edf0fc401
URL:		http://qt-project.org/
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt5 qtdoc package contains the main Qt Reference Documentation, which
includes overviews, Qt topics, and examples not specific to any Qt
module.

%description -l pl.UTF-8
Pakiet Qt5 qtdoc zawiera podstawową część dokumentacji referencyjnej
Qt, obejmującą artykuły przeglądowe, tematy związane z Qt oraz
przykłady niespecyficzne dla żadnego modułu Qt.

%package qch
Summary:	The Qt5 qtdoc documentation module - QCH format
Summary(pl.UTF-8):	Moduł dokumentacji Qt5 qtdoc - w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}

%description qch
The Qt5 qtdoc documentation module - QCH format.

%description qch -l pl.UTF-8
Moduł dokumentacji Qt5 qtdoc - w formacie QCH.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dist/changes-*
%{_docdir}/qt5-doc/qtdoc

%if %{with qch}
%files qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtdoc.qch
%endif
