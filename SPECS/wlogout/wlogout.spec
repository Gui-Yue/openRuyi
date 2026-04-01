# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wlogout
Version:        1.2.2
Release:        %autorelease
Summary:        A wayland based logout menu
License:        MIT
URL:            https://github.com/ArtsyMacaw/wlogout
#!RemoteAsset:  sha256:4c9204bfa19c73f51176c94c67711f54f3e393301c0809c61ae379054060fa46
Source0:        https://github.com/ArtsyMacaw/wlogout/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  bash-completion

%description
A wayland based logout menu. It supports custom styling and is designed
to be simple and easily configurable.

%files
%license LICENSE
%doc README.md
%{_bindir}/wlogout
%{_mandir}/man1/wlogout.1*
%{_mandir}/man5/wlogout.5*
%dir %{_sysconfdir}/wlogout
%config(noreplace) %{_sysconfdir}/wlogout/*
%{_datadir}/wlogout/
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_wlogout
%{_datadir}/fish/completions/wlogout.fish
%{bash_completions_dir}/wlogout.bash

%changelog
%autochangelog
