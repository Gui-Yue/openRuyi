# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jansson
Version:        2.14.1
Release:        %autorelease
Summary:        A C library for encoding, decoding and manipulating JSON data
License:        MIT
URL:            https://www.digip.org/jansson/
#!RemoteAsset
Source0:        https://github.com/akheron/jansson/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  bzip2
BuildSystem:    autotools
BuildOption(conf): --disable-static

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.

%package        devel
Summary:        files for jansson development
Requires:       %{name} = %{version}-%{release}
%description    devel
files for jansson development

%files
%license LICENSE
%{_libdir}/libjansson.so.*

%files devel
%license LICENSE
%doc CHANGES
%{_libdir}/libjansson.so
%{_libdir}/pkgconfig/jansson.pc
%{_includedir}/jansson*.h

%changelog
%{?autochangelog}
