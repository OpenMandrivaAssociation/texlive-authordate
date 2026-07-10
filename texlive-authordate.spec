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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Authordate produces styles loosely based on the recommendations of
British Standard 1629(1976), Butcher's Copy-editing and the Chicago
Manual of Style. The bundle provides four BibTeX styles (authordate1,
..., authordate4), and a LaTeX package, for citation in author/date
style. The BibTeX styles differ in how they format names and titles; one
of them is necessary for the LaTeX package to work.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/authordate
%dir %{_datadir}/texmf-dist/doc/bibtex/authordate
%dir %{_datadir}/texmf-dist/tex/latex/authordate
%{_datadir}/texmf-dist/bibtex/bst/authordate/authordate1.bst
%{_datadir}/texmf-dist/bibtex/bst/authordate/authordate2.bst
%{_datadir}/texmf-dist/bibtex/bst/authordate/authordate3.bst
%{_datadir}/texmf-dist/bibtex/bst/authordate/authordate4.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/README
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/authordate1.ltx
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/authordate2.ltx
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/authordate3.ltx
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/authordate4.ltx
%doc %{_datadir}/texmf-dist/doc/bibtex/authordate/testadb.ltx
%{_datadir}/texmf-dist/tex/latex/authordate/authordate1-4.sty
