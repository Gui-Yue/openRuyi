# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname peft

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        Parameter-Efficient Fine-Tuning of large pretrained models
License:        Apache-2.0
URL:            https://github.com/huggingface/peft
VCS:            git:https://github.com/huggingface/peft
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l peft
BuildOption(check):  -e 'peft.tuners.*.bnb' -e peft.tuners.lora.corda

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(accelerate) >= 0.21
BuildRequires:  python3dist(huggingface-hub) >= 0.25
BuildRequires:  python3dist(numpy) >= 1.17
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(safetensors)
BuildRequires:  python3dist(torch) >= 1.13
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(transformers)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
PEFT provides methods for parameter-efficient fine-tuning of large models.

%files -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
