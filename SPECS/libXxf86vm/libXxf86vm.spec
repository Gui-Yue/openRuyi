# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Icenowy Zheng <uwu@icenowy.me>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libXxf86vm
Version:        1.1.6
Release:        %autorelease
Summary:        X library wrapping the XFree86-VidMode extension
License:        MIT
URL:            https://www.x.org/
#!RemoteAsset
Source:         https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz

BuildSystem:    autotools
BuildOption(conf): --disable-static

BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11) >= 1.6
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xf86vidmodeproto) >= 2.2.99.1

%description
X11 helper library for accessing the XFree86-VidMode procotol extension.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
%{name} development package

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libXxf86vm.so.*

%files devel
%{_includedir}/X11/extensions/xf86vmode.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libXxf86vm.so
%{_mandir}/man3/*

%changelog
%{?autochangelog}
