# Create your models here.
from django.db import models
from datetime import *
from django.db import models

class TableStructure(models.Model):
    inputEnter = models.CharField(max_length=25000)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=25000)
    slug = models.CharField(max_length=25000)
    solutionTitle = models.CharField(max_length=25000)
    date_modified = models.DateTimeField() 
 
    class Meta:
        abstract = True
 
    def __str__(self):
        """A string representation of the model."""
        return self.solutionTitle[:50]


class add_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "add_poly_db"
class sub_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "sub_poly_db"
class mul_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "mul_poly_db"
class div_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "div_poly_db"
class check_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "check_poly_db"
class degree_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "degree_poly_db"
class ascding_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "ascding_poly_db"
class descding_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "descding_poly_db"
class leading_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "leading_poly_db"
class fact_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "fact_poly_db"
class gcf_poly_db(TableStructure):
    class Meta:
        verbose_name_plural = "gcf_poly_db"
class gcf_fact_db(TableStructure):
    class Meta:
        verbose_name_plural = "gcf_fact_db"
class poly_lcm_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_lcm_db"
class poly_prime_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_prime_db"
class poly_fact_cube_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_fact_cube_db"
class poly_fact_sqr_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_fact_sqr_db"
class binom_expn_db(TableStructure):
    class Meta:
        verbose_name_plural = "binom_expn_db"
class fact_complex_db(TableStructure):
    class Meta:
        verbose_name_plural = "fact_complex_db"
class poly_root_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_root_db"
class poly_remainer_db(TableStructure):
    class Meta:
        verbose_name_plural = "poly_remainer_db"
