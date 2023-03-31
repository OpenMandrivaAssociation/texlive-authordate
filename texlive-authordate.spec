Name:		texlive-authordate
Version:	52564
Release:	2
Summary:	Author/date style citation styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/authordate
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authordate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authordate.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Authordate produces styles loosely based on the recommendations
of British Standard 1629(1976), Butcher's Copy-editing and the
Chicago Manual of Style. The bundle provides four BibTeX styles
(authordate1, ..., authordate4), and a LaTeX package, for
citation in author/date style. The BibTeX styles differ in how
they format names and titles; one of them is necessary for the
LaTeX package to work.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/authordate
%{_texmfdistdir}/bibtex/bst/authordate
%doc %{_texmfdistdir}/doc/bibtex/authordate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
