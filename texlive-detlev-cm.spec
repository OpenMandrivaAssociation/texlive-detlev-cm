# revision 32383
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-detlev-cm
Version:	20140216
Release:	3
Summary:	TeXLive detlev-cm package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detlev-cm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detlev-cm.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive detlev-cm package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/detlev-cm/beamercolorthemeETII.sty
%{_texmfdistdir}/tex/latex/detlev-cm/beamerfontthemeDetlevCM.sty
%{_texmfdistdir}/tex/latex/detlev-cm/beamerouterthemeDetlevCM.sty
%{_texmfdistdir}/tex/latex/detlev-cm/beamerthemeDetlevCM.sty
%doc %{_texmfdistdir}/doc/latex/detlev-cm/LogoTop.png
%doc %{_texmfdistdir}/doc/latex/detlev-cm/SAS-CRJ900.png
%doc %{_texmfdistdir}/doc/latex/detlev-cm/Sample.pdf
%doc %{_texmfdistdir}/doc/latex/detlev-cm/Sample.tex
%doc %{_texmfdistdir}/doc/latex/detlev-cm/Wing.png
%doc %{_texmfdistdir}/doc/latex/detlev-cm/WingSunrise.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
