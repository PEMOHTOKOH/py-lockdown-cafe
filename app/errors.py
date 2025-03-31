class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return f"NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return f"OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __str__(self):
        return f"NotWearingMaskError"