# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname warc3-wet-clueweb09
%global module warc3_wet_clueweb09

Name:           python-%{srcname}
Version:        0.2.5
Release:        %autorelease
Summary:        ARC and WARC reader with ClueWeb09 fixes
License:        GPL-2.0-only
URL:            https://github.com/seanmacavaney/warc3-clueweb
VCS:            git:https://github.com/seanmacavaney/warc3-clueweb
#!RemoteAsset:  sha256:3054bfc07da525d5967df8ca3175f78fa3f78514c82643f8c81fbca96300b836
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{module}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
warc3-wet-clueweb09 reads ARC and WARC files with fixes for ClueWeb09 data.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc Readme.rst
%license LICENSE

%changelog
%autochangelog
