%global tl_name authordate
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Author/date style citation styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/authordate
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authordate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authordate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Authordate produces styles loosely based on the recommendations of
British Standard 1629(1976), Butcher's Copy-editing and the Chicago
Manual of Style. The bundle provides four BibTeX styles (authordate1,
..., authordate4), and a LaTeX package, for citation in author/date
style. The BibTeX styles differ in how they format names and titles; one
of them is necessary for the LaTeX package to work.

