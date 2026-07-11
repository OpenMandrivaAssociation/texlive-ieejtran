%global tl_name ieejtran
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19
Release:	%{tl_revision}.1
Summary:	Unofficial bibliography style file for the Institute of Electrical Engineers ...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/ieejtran
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ieejtran.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ieejtran.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an unofficial BibTeX style for authors of the
Institute of Electrical Engineers of Japan (IEEJ) transactions journals
and conferences.

