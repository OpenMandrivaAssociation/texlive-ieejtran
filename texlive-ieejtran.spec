Name:		texlive-ieejtran
Version:	62957
Release:	2
Summary:	Unofficial bibliography style file for the Institute of Electrical Engineers of Japan
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ieejtran
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieejtran.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ieejtran.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an unofficial BibTeX style for authors of
the Institute of Electrical Engineers of Japan (IEEJ)
transactions journals and conferences.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/ieejtran
%doc %{_texmfdistdir}/doc/bibtex/ieejtran

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
