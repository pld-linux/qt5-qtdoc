%define		orgname		qtdoc
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 qtdoc documentation module
Summary(pl.UTF-8):	Moduł dokumentacji Qt5 qtdoc
Name:		qt5-%{orgname}
Version:	5.15.2
Release:	2
License:	FDL v1.3
Group:		Documentation
Source0:	http://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-src-%{version}.tar.xz
# Source0-md5:	90de2911fa80c7668ec7289d5768e802
URL:		https://www.qt.io/
BuildRequires:	qt5-assistant >= %{qttools_ver}
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

%package demos
Summary:	The Qt5 qtdoc documentation module - demos
Summary(pl.UTF-8):	Moduł dokumentacji Qt5 qtdoc - programy demonstracyjne
License:	BSD or commercial
Group:		Documentation

%description demos
The Qt5 qtdoc documentation module - demos.

%description demos -l pl.UTF-8
Moduł dokumentacji Qt5 qtdoc - programy demonstracyjne.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# remove compiled binaries, let demos be noarch
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/qt5/demos/{calqlatr/calqlatr,clocks/clocks,maroon/maroon,photosurface/photosurface,rssnews/rssnews,samegame/samegame,stocqt/stocqt,tweetsearch/tweetsearch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dist/changes-*
%{_docdir}/qt5-doc/qtcmake
%{_docdir}/qt5-doc/qtdoc

%files qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtcmake.qch
%{_docdir}/qt5-doc/qtdoc.qch

%files demos
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%{_examplesdir}/qt5/demos
