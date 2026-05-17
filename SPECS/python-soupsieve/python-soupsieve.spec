# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname soupsieve

Name:           python-%{srcname}
Version:        2.8.3
Release:        %autorelease
Summary:        Modern CSS selector implementation for Beautiful Soup
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
VCS:            git:https://github.com/facelessuser/soupsieve
#!RemoteAsset:  sha256:3267f1eeea4251fb42728b6dfb746edc9acaffc4a45b27e19450b676586e8349
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%check
# Importing soupsieve imports bs4, but beautifulsoup4 depends on soupsieve.

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
