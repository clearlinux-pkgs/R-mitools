#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mitools
Version  : 2.4
Release  : 41
URL      : https://cran.r-project.org/src/contrib/mitools_2.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mitools_2.4.tar.gz
Summary  : Tools for Multiple Imputation of Missing Data
Group    : Development/Tools
License  : GPL-2.0
Requires: R-DBI
BuildRequires : R-DBI
BuildRequires : buildreq-R

%description
multiple-imputation datasets.

%prep
%setup -q -c -n mitools
cd %{_builddir}/mitools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641060470

%install
export SOURCE_DATE_EPOCH=1641060470
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mitools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mitools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mitools/DESCRIPTION
/usr/lib64/R/library/mitools/INDEX
/usr/lib64/R/library/mitools/Meta/Rd.rds
/usr/lib64/R/library/mitools/Meta/data.rds
/usr/lib64/R/library/mitools/Meta/demo.rds
/usr/lib64/R/library/mitools/Meta/features.rds
/usr/lib64/R/library/mitools/Meta/hsearch.rds
/usr/lib64/R/library/mitools/Meta/links.rds
/usr/lib64/R/library/mitools/Meta/nsInfo.rds
/usr/lib64/R/library/mitools/Meta/package.rds
/usr/lib64/R/library/mitools/Meta/vignette.rds
/usr/lib64/R/library/mitools/NAMESPACE
/usr/lib64/R/library/mitools/NEWS
/usr/lib64/R/library/mitools/R/mitools
/usr/lib64/R/library/mitools/R/mitools.rdb
/usr/lib64/R/library/mitools/R/mitools.rdx
/usr/lib64/R/library/mitools/data/pisamaths.rda
/usr/lib64/R/library/mitools/data/smi.rda
/usr/lib64/R/library/mitools/demo/mi.R
/usr/lib64/R/library/mitools/doc/index.html
/usr/lib64/R/library/mitools/doc/smi.R
/usr/lib64/R/library/mitools/doc/smi.Rnw
/usr/lib64/R/library/mitools/doc/smi.pdf
/usr/lib64/R/library/mitools/dta/smif1.dta
/usr/lib64/R/library/mitools/dta/smif2.dta
/usr/lib64/R/library/mitools/dta/smif3.dta
/usr/lib64/R/library/mitools/dta/smif4.dta
/usr/lib64/R/library/mitools/dta/smif5.dta
/usr/lib64/R/library/mitools/dta/smim1.dta
/usr/lib64/R/library/mitools/dta/smim2.dta
/usr/lib64/R/library/mitools/dta/smim3.dta
/usr/lib64/R/library/mitools/dta/smim4.dta
/usr/lib64/R/library/mitools/dta/smim5.dta
/usr/lib64/R/library/mitools/help/AnIndex
/usr/lib64/R/library/mitools/help/aliases.rds
/usr/lib64/R/library/mitools/help/mitools.rdb
/usr/lib64/R/library/mitools/help/mitools.rdx
/usr/lib64/R/library/mitools/help/paths.rds
/usr/lib64/R/library/mitools/html/00Index.html
/usr/lib64/R/library/mitools/html/R.css
