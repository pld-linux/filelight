Summary:	Graphical disk usage statistics
Summary(pl.UTF-8):	Graficzne statystyki zajęcia dysku
Name:		filelight
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.methylblue.com/filelight/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	aa885e53e09f40e7fdd371395140b957
Source1:	http://www.methylblue.com/filelight/packages/%{name}-%{version}-i18n-20060901.tar.bz2
# Source1-md5:	7e556cbb36da96afa8105deb50840989
Patch0:		kde-ac260-lt.patch
URL:		http://www.methylblue.com/filelight/
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filelight graphically represents a file system as a set of concentric
segmented-rings, indicating where diskspace is being used. Segments
expanding from the center represent files (including directories),
with each segment's size being proportional to the file's size and
directories having child segments. Filelight performs a similar
function to KDirstat, but in a more compact fashion.

%description -l pl.UTF-8
Filelight przedstawia graficznie system plików jako zbiór koncentrycznych, 
posegmentowanych pierścieni, wskazujących gdzie przestrzeń dyskowa jest 
używana. Segmenty, rozchodzące się od środka, reprezentują pliki (włączając
w to katalogi), a rozmiar każdego z nich jest proporcjonalny do rozmiaru pliku,
natomiast katalogi zawierają segmenty-dzieci. Filelight posiada funkcjonalność
zbliżoną do KDirstat, ale w bardziej zwięzłej formie.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__make} -f admin/Makefile.common
%configure
%{__make}

cd %{name}-%{version}-i18n-20060901
%configure
cd po
find . -name '*.gmo' -exec rm {} \;
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd %{name}-%{version}-i18n-20060901/po
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd -

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/%{name}
%{_datadir}/config/*
%{_datadir}/services/*
%{_iconsdir}/*/*/*/*.png
%%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
