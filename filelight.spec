Summary:	Graphical disk usage statistics
Summary(pl):	Graficzne statystyki zajêcia dysku
Name:		filelight
Version:	0.6.4
Release:	1
License:	GPL
Vendor:		Max Howell <max.howell@methylblue.com>
Group:		X11/Applications
Source0:	http://www.methylblue.com/filelight/%{name}-%{version}.tar.gz
# Source0-md5:	a45ded39158a3de9762aae1a8333f768
URL:		http://www.methylblue.com/filelight/
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filelight graphically represents a file system as a set of concentric
segmented-rings, indicating where diskspace is being used. Segments
expanding from the center represent files (including directories),
with each segment's size being proportional to the file's size and
directories having child segments. Filelight performs a similar
function to KDirstat, but in a more compact fashion.

%description -l pl
Filelight przedstawia graficznie system plików jako zbiór koncentrycznych, 
posegmentowanych pier¶cieni, wskazuj±cych gdzie przestrzeñ dyskowa jest 
u¿ywana. Segmenty, rozchodz±ce siê od ¶rodka, reprezentuj± pliki (w³±czaj±c
w to katalogi), a rozmiar ka¿dego z nich jest proporcjonalny do rozmiaru pliku,
natomiast katalogi zawieraj± segmenty-dzieci. Filelight posiada funkcjonalno¶æ
zbli¿on± do KDirstat, ale w bardziej zwiêz³ej formie.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--prefix `kde-config --prefix`  \
	--enable-final \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT{%{_datadir}/Utilities,%{_desktopdir}}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/config/%{name}rc
%{_iconsdir}/*/*/apps/%{name}.png
