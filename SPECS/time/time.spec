# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global optflags %optflags -Wno-error=incompatible-pointer-types

Name:           time
Version:        1.9
Release:        %autorelease
Summary:        Run Programs And Summarize System Resource Usage
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/time/
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/time/%{name}-%{version}.tar.gz
#!RemoteAsset
Source2:        https://ftpmirror.gnu.org/gnu/time/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

%description
The "time" command runs another program, then displays information
about the resources used by that program, collected by the system
while the program was running.

%install -a
install -d %{buildroot}%{_mandir}/man1

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/time
%{_infodir}/time.info*

%changelog
%{?autochangelog}
