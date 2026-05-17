# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname trec-car-tools
%global module trec_car

Name:           python-%{srcname}
Version:        2.6
Release:        %autorelease
Summary:        Support tools for TREC CAR participants
License:        BSD-3-Clause
URL:            https://github.com/TREMA-UNH/trec-car-tools/python3
VCS:            git:https://github.com/TREMA-UNH/trec-car-tools
#!RemoteAsset:  sha256:2fce2de120224fd569b151d5bed358a4ed334e643889b9e3dfe3e5a3d15d21c8
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{module}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(cbor) >= 1.0.0
BuildRequires:  python3dist(numpy) >= 1.11.2
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
trec-car-tools contains support utilities for TREC Complex Answer Retrieval.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}

%changelog
%autochangelog
