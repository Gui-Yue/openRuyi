# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tabulate

Name:           python-%{srcname}
Version:        0.10.0
Release:        %autorelease
Summary:        Pretty-print tabular data in Python, a library and a command-line utility
License:        MIT
URL:            https://github.com/astanin/python-tabulate
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The main use cases of the library are:

• printing small tables without hassle: just one function call, formatting is
  guided by the data itself
• authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
• readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG
%doc README.md
%{_bindir}/tabulate

%changelog
%autochangelog
