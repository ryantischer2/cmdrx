Name:           cmdrx
Version:        0.1.0
Release:        1%{?dist}
Summary:        AI-powered command line troubleshooting tool

License:        MIT
URL:            https://github.com/cmdrx/cmdrx
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

Requires:       python3
Requires:       python3-click >= 8.0.0
Requires:       python3-rich >= 13.0.0
Requires:       python3-requests >= 2.28.0
Requires:       python3-keyring >= 24.0.0
Requires:       python3-openai >= 1.0.0
Requires:       python3-cryptography >= 3.4.0
Requires:       python3-pydantic >= 2.0.0

%description
CmdRx is a command line tool designed to assist IT personnel in analyzing
CLI command outputs and providing troubleshooting steps and suggested fixes
using artificial intelligence.

Features:
- Multiple input modes (standalone and piped)
- Support for multiple LLM providers (OpenAI, Anthropic, Grok, custom)
- Secure credential storage using system keyring
- Detailed logging and automated fix script generation
- Text-based configuration interface

This tool helps system administrators quickly diagnose and resolve issues
with Linux commands and services by leveraging the power of large language
models.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

# Install man page
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c docs/cmdrx.1 > %{buildroot}%{_mandir}/man1/cmdrx.1.gz

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_bindir}/cmdrx
%{_mandir}/man1/cmdrx.1.gz

%changelog
* Mon Dec 01 2024 CmdRx Team <team@cmdrx.dev> - 0.1.0-1
- Initial release
- Support for multiple LLM providers
- Secure credential storage
- Text-based configuration interface
- Automated fix script generation