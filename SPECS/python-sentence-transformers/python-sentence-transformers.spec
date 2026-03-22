# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentence-transformers

Name:           python-%{srcname}
Version:        5.3.0
Release:        %autorelease
Summary:        Embeddings, retrieval, and reranking toolkit
License:        Apache-2.0
URL:            https://www.sbert.net
VCS:            git:https://github.com/UKPLab/sentence-transformers
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/sentence_transformers-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l sentence_transformers

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  (python3dist(transformers) < 6~~ with python3dist(transformers) >= 4.41)
BuildRequires:  python3dist(huggingface-hub) >= 0.20
BuildRequires:  python3dist(torch) >= 1.11
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scikit-learn)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(typing-extensions) >= 4.5

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Sentence Transformers provides sentence and text embedding models.

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
