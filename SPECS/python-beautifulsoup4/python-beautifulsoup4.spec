# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname beautifulsoup4
%global module bs4

Name:           python-%{srcname}
Version:        4.14.3
Release:        %autorelease
Summary:        Screen-scraping library
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
# VCS: No VCS link available
#!RemoteAsset:  sha256:6292b1c5186d356bba669ef9f7f051757099565ad9ada5dd630bd9de5fa7fb86
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{module}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(soupsieve) >= 1.6.1
BuildRequires:  python3dist(typing-extensions) >= 4.0.0

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Beautiful Soup is a library for pulling data out of HTML and XML files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS CHANGELOG README.md
%license LICENSE

%changelog
%autochangelog
