# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname inscriptis

Name:           python-%{srcname}
Version:        2.7.1
Release:        %autorelease
Summary:        HTML to text converter
License:        Apache-2.0
URL:            https://github.com/weblyzard/inscriptis
VCS:            git:https://github.com/weblyzard/inscriptis
#!RemoteAsset:  sha256:16517bab88ac2c8f01d58748bf070256e8af7a3fac96d1e317b01371d04a3c6e
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(lxml) >= 5.4.0
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests) >= 2.32.3

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Inscriptis converts HTML documents into clean plain text.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS README.rst
%license LICENSE

%changelog
%autochangelog
