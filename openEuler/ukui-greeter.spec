%define debug_package %{nil}
Name:           ukui-greeter
Version:        3.0.1
Release:        4
Summary:        Lightdm greeter for UKUI
License:        GPL-2.0
URL:            http://www.ukui.org
Source0:        ukui-greeter-%{version}.tar.gz

BuildRequires: pkgconf
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: lightdm-qt5-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libXrandr-devel
BuildRequires: qt5-qttools-devel
BuildRequires: imlib2-devel

Provides: lightdm-greeter

%description
A greeter for UKUI desktop environment written by Qt5.
 The greeter supports biometric authentication which is
 provided by biometric-authentication service.

%prep
%setup -q

%build
qmake-qt5
make

%install
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/usr/share/man/man8/
gzip  -c ukui-greeter/man/ukui-greeter.8 > %{buildroot}/usr/share/man/man8/ukui-greeter.8.gz

%clean
##[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%doc  debian/copyright debian/changelog
%{_sysconfdir}/lightdm/ukui-greeter.conf
%{_datadir}/man/man8/ukui-greeter.8.gz
%{_sbindir}/ukui-greeter
%{_datadir}/lightdm/lightdm.conf.d/95-ukui-greeter.conf
%{_datadir}/ukui-greeter/
%{_datadir}/xgreeters/ukui-greeter.desktop

%changelog
* Wed Feb 3 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-4
- update to upstream version 3.0.1-1

* Tue Dec 8 2020 lvhan <lvhan@kylinos.cn> - 3.0.1-3
- 0001-fix-icon-misplaced.patch

* Tue Dec 8 2020 douyan <douyan@kylinos.cn> - 3.0.1-2
- 0002-fix-ukui-greeter-desktop-option-issue.patch

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update 3.0.0-1+1026

* Mon Jul 20 2020 douyan <douyan@kylinos.cn> - 1.2.5-1
- update 1.2.5

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.3-1
- Init package for openEuler
