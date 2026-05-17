# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname warc3-wet
%global pypi_name warc3_wet
%global module warc

Name:           python-%{srcname}
Version:        0.2.5
Release:        %autorelease
Summary:        Python library to work with ARC and WARC files
License:        GPL-2.0-only
URL:            https://github.com/Willian-Zhang/warc3
VCS:            git:https://github.com/Willian-Zhang/warc3
#!RemoteAsset:  sha256:15e50402dabaa1e95307f1e2a6169cfd5f137b70761d9f0b16a10aa6de227970
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
warc3-wet is a Python library for reading ARC and WARC web archive files.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc Readme.rst
%license LICENSE

%changelog
%autochangelog
