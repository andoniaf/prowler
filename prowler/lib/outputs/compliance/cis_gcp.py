from prowler.config.config import timestamp
from prowler.lib.outputs.models import Check_Output_CSV_GCP_CIS, generate_csv_fields
from prowler.lib.utils.utils import outputs_unix_timestamp


def generate_compliance_row_cis_gcp(
    finding, compliance, requirement, attribute, output_options
):
    compliance_row = Check_Output_CSV_GCP_CIS(
        Provider=finding.check_metadata.Provider,
        Description=compliance.Description,
        ProjectId=finding.project_id,
        Location=finding.location.lower(),
        AssessmentDate=outputs_unix_timestamp(output_options.unix_timestamp, timestamp),
        Requirements_Id=requirement.Id,
        Requirements_Description=requirement.Description,
        Requirements_Attributes_Section=attribute.Section,
        Requirements_Attributes_Profile=attribute.Profile,
        Requirements_Attributes_AssessmentStatus=attribute.AssessmentStatus,
        Requirements_Attributes_Description=attribute.Description,
        Requirements_Attributes_RationaleStatement=attribute.RationaleStatement,
        Requirements_Attributes_ImpactStatement=attribute.ImpactStatement,
        Requirements_Attributes_RemediationProcedure=attribute.RemediationProcedure,
        Requirements_Attributes_AuditProcedure=attribute.AuditProcedure,
        Requirements_Attributes_AdditionalInformation=attribute.AdditionalInformation,
        Requirements_Attributes_References=attribute.References,
        Status=finding.status,
        StatusExtended=finding.status_extended,
        ResourceId=finding.resource_id,
        ResourceName=finding.resource_name,
        CheckId=finding.check_metadata.CheckID,
    )
    csv_header = generate_csv_fields(Check_Output_CSV_GCP_CIS)

    return compliance_row, csv_header
