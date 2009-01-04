#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	VectorReal
Summary:	Math::VectorReal - Module to handle 3D Vector Mathematics
#Summary(pl.UTF-8):	
Name:		perl-Math-VectorReal
Version:	1.02
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9eacc7b8dffeedd1d9cce2ed1c803ba4
URL:		http://search.cpan.org/dist/Math-VectorReal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Math::VectorReal package defines a 3D mathematical "vector", in a way
that is compatible with the previous CPAN module Math::MatrixReal. However
it provides a more vector oriented set of mathematical functions and overload
operators, to the MatrixReal package.  For example the normal perl string
functions "x" and "." have been overloaded to allow vector cross and dot
product operations. Vector math formula thus looks like vector math formula in
perl programs using this package.

While this package is compatible with Math::MatrixReal, you DO NOT need to
have that package to perform purely vector orientated calculations. You will
need it however if you wish to do matrix operations with these vectors. The
interface has been designed with this package flexibility in mind.

The vectors are defined in the same way as a "row" Math::MatrixReal matrix,
instead of that packages choice of "column" definition for vector operations.
Such vectors are multiplied to matices with the vector on the left and the
matrix on the right. EG:   v * M -> 'v

Not only is this the way I prefer to handle vectors, but it is the way most
graphics books use vectors. As a bonus it results in no overload conflicts
between this package and that of Math::MatrixReal, (the left objects overload
operator is called to do the mathematics). It also is a lot simpler than
MatrixReal column vector methods, which were designed for equation solving
rather than 3D geometry operations.

The  vector_matrix()  function provided, simplifies the creation a
MatrixReal object from 3 (usually orthogonal) vectors. This with its vector
orientated math operators makes it very easy to define orthogonal rotation
matrices from Math::VectorReal objects.  See a rough example in the
synopsis above, or in the file "matrix_test" in the packages source.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Math/*.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/*.pm
#%%{perl_vendorlib}/Math/VectorReal
%{_mandir}/man3/*
