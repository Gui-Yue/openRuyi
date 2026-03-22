# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentencepiece

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        Unsupervised text tokenizer and detokenizer for neural NLP
License:        Apache-2.0
URL:            https://github.com/google/sentencepiece
VCS:            git:https://github.com/google/sentencepiece
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  sentencepiece

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
SentencePiece is an unsupervised text tokenizer and detokenizer for neural NLP.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
