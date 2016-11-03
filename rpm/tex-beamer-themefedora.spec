%global commit0 bad52ddbea8a446b36e2b409afb938eeb33aeb4d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global texname beamer-themefedora

%{!?_texdir: %global _texdir %{_datadir}/texlive}

Name:           tex-%{texname}
Version:        0
Release:        0.1.%{shortcommit0}%{?dist}
Summary:        Red Hat beamer template

License: GPLv3+ and Commercial
URL: https://github.com/fale/beamer-themefedora
Source0: https://github.com/fale/beamer-themefedora/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch: noarch
BuildRequires: coreutils

Requires: texlive-scheme-minimal
Requires: texlive-xetex
Requires: texlive-xetex-def
Requires: texlive-beamer
Requires: texlive-euenc
Requires: overpass-fonts

%description
Fedora beamer temaplate

%prep
%setup -n %{texname}-%{commit0}

%install
mkdir -p %{buildroot}/%{_texdir}/texmf-dist/tex/latex/%{texname}
cp src/* %{buildroot}/%{_texdir}/texmf-dist/tex/latex/%{texname}

%post
mkdir -p /var/run/texlive
touch /var/run/texlive/run-texhash
touch /var/run/texlive/run-mtxrun
:

%postun
if [ $1 == 1 ]; then
  mkdir -p /var/run/texlive
  touch /var/run/texlive/run-texhash
else
  %{_bindir}/texhash 2> /dev/null
fi
:

%posttrans
if [ -e /var/run/texlive/run-texhash ] && [ -e %{_bindir}/texhash ]; then %{_bindir}/texhash 2> /dev/null; rm -f /var/run/texlive/run-texhash; fi
if [ -e /var/run/texlive/run-mtxrun ]; then export TEXMF=/usr/share/texlive/texmf-dist; export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c; export TEXMFCACHE=/var/lib/texmf; %{_bindir}/mtxrun --generate &> /dev/null; rm -f /var/run/texlive/run-mtxrun; fi
:

%files
%dir %{_texdir}/texmf-dist/tex/latex/%{texname}
%{_texdir}/texmf-dist/tex/latex/%{texname}/background.png
%{_texdir}/texmf-dist/tex/latex/%{texname}/fedora.sty
%{_texdir}/texmf-dist/tex/latex/%{texname}/fedora.png
%{_texdir}/texmf-dist/tex/latex/%{texname}/fedora-long.png

%changelog
* Thu Nov 03 2016 Fabio Alessandro Locati <fale@redhat.com> - 0.0-0.1.bad52dd
- Initial package
